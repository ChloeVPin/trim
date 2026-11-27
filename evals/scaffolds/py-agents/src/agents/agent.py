from dataclasses import dataclass, field
from typing import Any, Callable


@dataclass
class Agent:
    name: str
    instructions: str = ""
    tools: list[Callable[..., Any]] = field(default_factory=list)
    model: str | None = None
