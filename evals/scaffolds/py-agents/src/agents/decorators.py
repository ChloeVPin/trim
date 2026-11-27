from typing import Any, Callable


def function_tool(fn: Callable[..., Any]) -> Callable[..., Any]:
    fn.__agents_tool__ = True
    return fn


tool = function_tool
