# mypy: ignore-errors

from __future__ import annotations

import os
import sys

from contextlib import nullcontext
from typing import TYPE_CHECKING

import ray
import ray.util.rpdb

from madbg.debugger import RemoteIPythonDebugger
from madbg.utils import use_context


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
            sock, _ = server_socket.accept()
        return cls.start_from_new_connection(sock)
