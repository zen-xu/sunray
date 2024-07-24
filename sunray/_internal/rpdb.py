# mypy: ignore-errors

from __future__ import annotations

import io
import os
import subprocess
import sys
import traceback

from contextlib import contextmanager
from contextlib import nullcontext
from contextlib import redirect_stdout
from termios import tcdrain
from typing import TYPE_CHECKING

import ray
import ray.util.rpdb

from IPython.core.alias import Alias
from madbg.communication import Piping
from madbg.communication import receive_message
from madbg.debugger import RemoteIPythonDebugger
from madbg.tty_utils import PTY
from madbg.utils import run_thread
from madbg.utils import use_context
from pdbr._pdbr import ANSI_ESCAPE
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

    if os.environ.get("SUNRAY_REMOTE_PDB", "yes").lower() in ["1", "yes", "true"]:
        set_trace_by_madbg(frame)
    else:
        set_trace_by_ray(frame, breakpoint_uuid)


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
                f"use 'sunray debug {ip} {server_socket.getsockname()[1]}' to connect...",
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
    debugger_class = rich_pdb_klass(
        RemoteDebugger,
        context={"term_type": term_type},
        console=Console(
            file=stdout,
            height=height,
            width=width,
            stderr=True,
            force_terminal=True,
            force_interactive=True,
            tab_size=4,
            theme=Theme(
                {"info": "dim cyan", "warning": "magenta", "danger": "bold red"}
            ),
        ),
        show_layouts=os.environ.get("SUNRAY_REMOTE_PDB_SHOW_LAYOUTS", "yes").lower()
        in ["1", "yes", "true"],
    )

    class Debugger(debugger_class):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self._theme = os.environ.get("SUNRAY_REMOTE_PDB_THEME", "ansi_dark")
            self.prompt = "sunray-pdb> "

        def _format_stack_entry(self, frame_lineno):
            entry = super()._format_stack_entry(frame_lineno)
            if len(entry.splitlines()) == 1:
                entry += "\n\n"
            return entry

        def print_stack_entry(self, frame_lineno, prompt_prefix="\n-> ", context=None):
            head = ANSI_ESCAPE.sub(
                "", self.format_stack_entry(frame_lineno, prompt_prefix)
            ).splitlines()[0]
            syntax = self._get_syntax_for_list()
            self._print(head, print_layout=False)
            self._print(syntax, print_layout=False)

        def do_help(self, arg):
            return RemoteDebugger.do_help(self, arg)

        def run_magic(self, line) -> str:
            magic_name, arg, line = self.parseline(line)
            result = stdout = ""
            if hasattr(self, f"do_{magic_name}"):
                # We want to use do_{magic_name} methods if defined.
                # This is indeed the case with do_pdef, do_pdoc etc,
                # which are defined by our base class (IPython.core.debugger.Pdb).
                result = getattr(self, f"do_{magic_name}")(arg)
            else:
                magic_fn = self.shell.find_line_magic(magic_name)
                if not magic_fn:
                    self.error(f"Line Magic %{magic_name} not found")
                    return ""

                if isinstance(magic_fn, Alias):
                    stdout, stderr = call_magic_fn(magic_fn, arg)
                    if stderr:
                        self.error(stderr)
                        return ""
                else:
                    std_buffer = io.StringIO()
                    with redirect_stdout(std_buffer):
                        if magic_name in ("time", "timeit"):
                            result = magic_fn(
                                arg,
                                local_ns={
                                    **self.curframe_locals,
                                    **self.curframe.f_globals,
                                },
                            )
                        else:
                            result = magic_fn(arg)
                    stdout = std_buffer.getvalue()
            if stdout:
                self._print(stdout.rstrip("\n"), print_layout=False)
            if result is not None:
                self._print(str(result), print_layout=False)
            return result

    debugger = Debugger(stdin=stdin, stdout=stdout)
    return debugger


def call_magic_fn(alias: Alias, rest):
    cmd = alias.cmd
    nargs = alias.nargs
    # Expand the %l special to be the user's input line
    if cmd.find("%l") >= 0:
        cmd = cmd.replace("%l", rest)
        rest = ""

    if nargs == 0:
        if cmd.find("%%s") >= 1:
            cmd = cmd.replace("%%s", "%s")
        # Simple, argument-less aliases
        cmd = f"{cmd} {rest}"
    else:
        # Handle aliases with positional arguments
        args = rest.split(None, nargs)
        if len(args) < nargs:
            raise RuntimeError(
                f"Alias <{alias.name}> requires {nargs} arguments, {len(args)} given."
            )
        cmd = "{} {}".format(cmd % tuple(args[:nargs]), " ".join(args[nargs:]))
    return subprocess.Popen(
        cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
    ).communicate()
