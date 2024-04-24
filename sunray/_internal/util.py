from __future__ import annotations

import inspect

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from typing import Callable


def get_num_returns(f: Callable) -> int:
    sig = inspect.signature(f)
    if getattr(sig.return_annotation, "__origin__", None) == tuple:
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
