from dataclasses import dataclass
from typing import Any

from .agent import Agent

DEFAULT_MAX_TURNS = 20


@dataclass
class RunConfig:
    model: str | None = None
    max_turns: int = DEFAULT_MAX_TURNS
    tracing_disabled: bool = False


@dataclass
class RunResult:
    final_output: Any
    turns: int


class Runner:
    @classmethod
    async def run(cls, agent: Agent, input: str, run_config: RunConfig | None = None) -> RunResult:
        config = run_config or RunConfig()
        model = config.model or agent.model
        turns = 0
        output: Any = None
        while turns < config.max_turns:
            turns += 1
            response = await _call_model(model, agent, input)
            for call in response.get("tool_calls", []):
                fn = next(t for t in agent.tools if t.__name__ == call["name"])
                result = fn(**call["arguments"])
                input = str(result)
            if response.get("final_output") is not None:
                output = response["final_output"]
                break
        return RunResult(final_output=output, turns=turns)


async def _call_model(model: str | None, agent: Agent, input: str) -> dict[str, Any]:
    raise NotImplementedError("model providers are not wired up in this checkout")
