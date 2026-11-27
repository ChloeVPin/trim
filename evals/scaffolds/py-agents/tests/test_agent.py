from agents import Agent


def test_agent_defaults():
    agent = Agent(name="a")
    assert agent.tools == []
    assert agent.model is None
