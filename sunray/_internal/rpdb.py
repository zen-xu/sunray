# mypy: ignore-errors

from __future__ import annotations

import os
import sys
import traceback

from contextlib import contextmanager
from contextlib import nullcontext
from termios import tcdrain
from typing import TYPE_CHECKING

import ray
import ray.util.rpdb

from madbg.communication import Piping
from madbg.communication import receive_message
from madbg.debugger import RemoteIPythonDebugger
from madbg.tty_utils import PTY
from madbg.utils import run_thread
from madbg.utils import use_context
from pdbr._pdbr import rich_pdb_klass
from rich.console import Console
from rich.theme import Theme


if TYPE_CHECKING:
    from contextlib import AbstractContextManager
    from types import FrameType

    from ray._private.worker import Worker


def get_global_worker() -> Worker:
    from ray._private.worker import global_worker

    return global_worker


def set_trace(breakpoint_uuid=None):
    """Interrupt the flow of the program and drop into the Ray debugger.

    Can be used within a Ray task or actor.
    """

    if ray.util.ray_debugpy._is_ray_debugger_enabled():
        return ray.util.ray_debugpy.set_trace(breakpoint_uuid)

    # If there is an active debugger already, we do not want to
    # start another one, so "set_trace" is just a no-op in that case.
    if get_global_worker().debugger_breakpoint != b"":
        return

    frame = sys._getframe().f_back

    if os.environ.get("DISABLE_MADBG", "").lower() in ["1", "yes", "true"]:
        set_trace_by_ray(frame, breakpoint_uuid)
    else:
        set_trace_by_madbg(frame)


def set_trace_by_ray(frame: FrameType | None, breakpoint_uuid: bytes | None):
    ray.util.rpdb._connect_ray_pdb(
        breakpoint_uuid=breakpoint_uuid.decode() if breakpoint_uuid else None,
        debugger_external=get_global_worker().ray_debugger_external,
    ).set_trace(frame=frame)


def set_trace_by_madbg(frame: FrameType | None):
    port = int(os.environ.get("REMOTE_PDB_PORT", "0"))
    ip: str = (
        get_global_worker().node_ip_address
        if get_global_worker().ray_debugger_external
        else os.environ.get("REMOTE_PDB_HOST", "localhost")
    )
    debugger, exit_stack = use_context(RemoteDebugger.connect_and_start(ip, port))
    debugger.set_trace(frame, done_callback=exit_stack.close)


class RemoteDebugger(RemoteIPythonDebugger):
    def __init__(self, stdin, stdout, context, **kwargs):
        from prompt_toolkit.input import vt100

        # fix annoying `Warning: Input is not a terminal (fd=0)`
        vt100.Vt100Input._fds_not_a_terminal.add(0)

        term_type = context["term_type"]
        super().__init__(stdin, stdout, term_type)

    @classmethod
    def connect_and_start(
        cls, ip: str, port: int
    ) -> AbstractContextManager[RemoteIPythonDebugger]:
        # TODO: get rid of context managers at some level - nobody is going to use with start() anyway
        current_instance = cls._get_current_instance()
        if current_instance is not None:
            return nullcontext(current_instance)
        with cls.get_server_socket(ip, port) as server_socket:
            server_socket.listen(1)
            print(
                f"RemotePdb session open at {ip}:{server_socket.getsockname()[1]}, "
                f"use 'madbg connect {ip} {server_socket.getsockname()[1]}' to connect...",
                file=sys.__stderr__,
                flush=True,
            )
            sock, address = server_socket.accept()
            print(
                f"RemotePdb accepted connection from {address}.",
                file=sys.__stderr__,
                flush=True,
            )
        return cls.start_from_new_connection(sock)

    @classmethod
    @contextmanager
    def start(cls, sock_fd: int):
        # TODO: just add to pipe list
        assert cls._get_current_instance() is None
        term_data = receive_message(sock_fd)
        term_attrs, term_type, term_size = (
            term_data["term_attrs"],
            term_data["term_type"],
            term_data["term_size"],
        )
        with PTY.open() as pty:
            pty.resize(term_size[0], term_size[1])
            pty.set_tty_attrs(term_attrs)
            pty.make_ctty()
            piping = Piping({sock_fd: {pty.master_fd}, pty.master_fd: {sock_fd}})
            with run_thread(piping.run):
                slave_reader = os.fdopen(pty.slave_fd, "r")
                slave_writer = os.fdopen(pty.slave_fd, "w")
                try:
                    instance = build_remote_debugger(
                        term_size, term_type, slave_reader, slave_writer
                    )
                    cls._set_current_instance(instance)
                    yield instance
                except Exception:
                    print(traceback.format_exc(), file=slave_writer)
                    raise
                finally:
                    cls._set_current_instance(None)
                    print("Closing connection", file=slave_writer, flush=True)
                    tcdrain(pty.slave_fd)
                    slave_writer.close()


def build_remote_debugger(term_size: tuple[int, int], term_type: str, stdin, stdout):
    height, width = term_size
    if os.environ.get("DISABLE_RPDB_COLOR", "").lower() in ["1", "yes", "true"]:
        debugger = RemoteDebugger(
            stdin=stdin, stdout=stdout, context={"term_type": term_type}
        )
    else:
        debugger = rich_pdb_klass(
            RemoteDebugger,
            context={"term_type": term_type},
            console=Console(
                file=stdout,
                height=height,
                width=width,
                force_terminal=True,
                force_interactive=True,
                tab_size=4,
                theme=Theme(
                    {"info": "dim cyan", "warning": "magenta", "danger": "bold red"}
                ),
            ),
        )(stdin=stdin, stdout=stdout)

    debugger.prompt = "ray-pdb> "
    return debugger
