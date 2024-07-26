from __future__ import annotations

import inspect

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from types import TracebackType
    from typing import Callable


def get_num_returns(f: Callable) -> int:
    sig = inspect.signature(f)
    if getattr(sig.return_annotation, "__origin__", None) is tuple:
        return len(sig.return_annotation.__args__)

    ret_annotation = str(sig.return_annotation)
    if isinstance(ret_annotation, str) and ret_annotation.lower().startswith("tuple["):
        import ast

        ret_ast = ast.parse(ret_annotation, mode="eval")
        try:
            return len(ret_ast.body.slice.value.elts)  # type: ignore[attr-defined]
        # fix in py3.11
        except AttributeError:  # pragma: no cover
            return len(ret_ast.body.slice.elts)  # type: ignore[attr-defined]
    return 1


def exception_auto_debugger() -> ExceptionAutoDebugger:  # pragma: no cover
    """
    Auto post-mortem debugging for exceptions.

    .. code-block:: python
        import sunray


        @sunray.remote
        def f():
            with sunray.exception_auto_debugger():
                value1 = 1
                value2 = 0
                return value1 / value2


        sunray.get(f.remote())
    """

    return ExceptionAutoDebugger()


class ExceptionAutoDebugger:  # pragma: no cover
    def __enter__(self) -> None: ...

    def __exit__(self, exc_type, exc_value, tb: TracebackType) -> None:
        if exc_type is not None:
            import traceback

            import sunray

            traceback.print_tb(tb)
            sunray.post_mortem(tb)
