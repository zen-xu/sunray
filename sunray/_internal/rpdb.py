# mypy: disable-error-code = import-untyped
from __future__ import annotations

import contextlib
import errno
import inspect
import json
import os
import socket
import sys
import time
import uuid

from pdb import Pdb
from typing import TYPE_CHECKING

import ray
import ray.util.rpdb

from ray._private import ray_constants
from ray.experimental.internal_kv import _internal_kv_del
from ray.experimental.internal_kv import _internal_kv_put
from ray.util.rpdb import _cry


if TYPE_CHECKING:
    from typing import ContextManager


def set_trace(breakpoint_uuid=None):
    """Interrupt the flow of the program and drop into the Ray debugger.

    Can be used within a Ray task or actor.
    """

    if ray.util.ray_debugpy._is_ray_debugger_enabled():
        return ray.util.ray_debugpy.set_trace(breakpoint_uuid)

    if os.environ.get("DISABLE_MADBG", "").lower() in ["1", "yes", "true"]:
        connect_ray_pdb = ray.util.rpdb._connect_ray_pdb
    else:
        connect_ray_pdb = _connect_ray_pdb

    # If there is an active debugger already, we do not want to
    # start another one, so "set_trace" is just a no-op in that case.
    if ray._private.worker.global_worker.debugger_breakpoint == b"":
        frame = sys._getframe().f_back
        rdb = connect_ray_pdb(
            host=None,
            port=None,
            quiet=None,
            breakpoint_uuid=breakpoint_uuid.decode() if breakpoint_uuid else None,
            debugger_external=ray._private.worker.global_worker.ray_debugger_external,
        )
        rdb.set_trace(frame=frame)


with contextlib.suppress(ImportError):
    from madbg.debugger import RemoteIPythonDebugger
    from madbg.utils import use_context

    class RemotePdb(Pdb):
        active_instance = None
        _ctx_manager: ContextManager[RemoteIPythonDebugger]

        def __init__(
            self,
            breakpoint_uuid: str,
            host: str,
            port: int,
            ip_address: str,
            quiet=False,
            **kwargs,
        ) -> None:
            self._breakpoint_uuid = breakpoint_uuid
            self._host = host
            self._port = port
            self._ip_address = ip_address
            self._quiet = quiet

            server_socket = socket.socket()
            server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
            server_socket.bind((host, port))
            self._listen_socket = server_socket

        def listen(self):
            self._listen_socket.listen(1)
            if not self._quiet:
                _cry(
                    f"RemotePdb session open at {self._ip_address}:{self._listen_socket.getsockname()[1]}, "
                    f"use 'madbg connect {self._ip_address} {self._listen_socket.getsockname()[1]}' to connect..."
                )
            sock, address = self._listen_socket.accept()
            self._listen_socket.close()

            if not self._quiet:
                _cry(f"RemotePdb accepted connection from {address!r}.")

            self._ctx_manager = RemoteDebugger.start_from_new_connection(sock)
            self.backup = []
            RemotePdb.active_instance = self

        def __restore(self):
            if self.backup and not self._quiet:
                _cry(f"Restoring streams: {self.backup} ...")
            for name, fh in self.backup:
                setattr(sys, name, fh)
            _, exit_stack = use_context(self._ctx_manager)
            exit_stack.close()
            RemotePdb.active_instance = None

        def do_quit(self, arg):
            self.__restore()
            debugger, _ = use_context(self._ctx_manager)
            return debugger.do_quit(arg)

        do_q = do_exit = do_quit

        def do_continue(self, arg):
            self.__restore()
            debugger, _ = use_context(self._ctx_manager)
            return debugger.do_continue(arg)

        do_c = do_cont = do_continue

        def set_trace(self, frame=None) -> None:
            if frame is None:
                frame = sys._getframe().f_back
            debugger, exit_stack = use_context(self._ctx_manager)
            try:
                debugger.set_trace(frame, done_callback=exit_stack.close)
            except OSError as exc:
                if exc.errno != errno.ECONNRESET:
                    raise

        def post_mortem(self, traceback=None):
            debugger, _ = use_context(self._ctx_manager)
            try:
                debugger.post_mortem(traceback)
            except OSError as exc:
                if exc.errno != errno.ECONNRESET:
                    raise

        def do_remote(self, arg):
            """remote
            Skip into the next remote call.
            """
            # Tell the next task to drop into the debugger.
            ray._private.worker.global_worker.debugger_breakpoint = (
                self._breakpoint_uuid
            )
            # Tell the debug loop to connect to the next task.
            data = json.dumps(
                {
                    "job_id": ray.get_runtime_context().get_job_id(),
                }
            )
            _internal_kv_put(
                f"RAY_PDB_CONTINUE_{self._breakpoint_uuid}",
                data,
                namespace=ray_constants.KV_NAMESPACE_PDB,
            )
            self.__restore()
            _, exit_stack = use_context(self._ctx_manager)
            exit_stack.close()
            return self.do_continue(arg)

        def do_get(self, arg):
            """get
            Skip to where the current task returns to.
            """
            ray._private.worker.global_worker.debugger_get_breakpoint = (
                self._breakpoint_uuid
            )
            self.__restore()
            _, exit_stack = use_context(self._ctx_manager)
            exit_stack.close()
            return self.do_continue(arg)

    class RemoteDebugger(RemoteIPythonDebugger):
        def __init__(self, stdin, stdout, term_type):
            from IPython.core.history import HistoryManager

            HistoryManager.enabled = False
            super().__init__(stdin, stdout, term_type)

        @classmethod
        @contextlib.contextmanager
        def start_from_new_connection(cls, sock: socket.socket):
            try:
                with cls.start(sock.fileno()) as debugger:
                    yield debugger
            except Exception:
                pass
            finally:
                cls._set_current_instance(None)
                sock.close()

        def do_continue(self, arg):
            """Overriding super to add a print"""
            self.done_callback()
            self.nosigint = True
            from IPython import get_ipython

            ipy = get_ipython()
            ipy.clear_instance()
            ipy.cleanup()

            return super().do_continue(arg)

        do_c = do_cont = do_continue


def _connect_ray_pdb(
    host=None,
    port=None,
    quiet=None,
    breakpoint_uuid=None,
    debugger_external=False,
):
    """
    Opens a remote PDB on first available port.
    """
    if debugger_external:
        assert not host, "Cannot specify both host and debugger_external"
        host = "0.0.0.0"
    elif host is None:
        host = os.environ.get("REMOTE_PDB_HOST", "127.0.0.1")
    if port is None:
        port = int(os.environ.get("REMOTE_PDB_PORT", "0"))
    if quiet is None:
        quiet = bool(os.environ.get("REMOTE_PDB_QUIET", ""))
    if not breakpoint_uuid:
        breakpoint_uuid = uuid.uuid4().hex
    ip_address = (
        ray._private.worker.global_worker.node_ip_address
        if debugger_external
        else "localhost"
    )

    rdb = RemotePdb(
        breakpoint_uuid=breakpoint_uuid,
        host=host,
        port=port,
        ip_address=ip_address,
        quiet=quiet,
    )
    sockname = rdb._listen_socket.getsockname()
    pdb_address = f"{ip_address}:{sockname[1]}"
    parentframeinfo = inspect.getouterframes(inspect.currentframe())[2]
    import traceback

    import setproctitle

    data = {
        "proctitle": setproctitle.getproctitle(),
        "pdb_address": pdb_address,
        "filename": parentframeinfo.filename,
        "lineno": parentframeinfo.lineno,
        "traceback": "\n".join(traceback.format_exception(*sys.exc_info())),
        "timestamp": time.time(),
        "job_id": ray.get_runtime_context().get_job_id(),
    }
    _internal_kv_put(
        f"RAY_PDB_{breakpoint_uuid}",
        json.dumps(data),
        overwrite=True,
        namespace=ray_constants.KV_NAMESPACE_PDB,
    )
    rdb.listen()
    _internal_kv_del(
        f"RAY_PDB_{breakpoint_uuid}", namespace=ray_constants.KV_NAMESPACE_PDB
    )
    return rdb
