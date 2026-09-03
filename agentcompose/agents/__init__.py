"""Agent management module for AgentCompose."""

from agentcompose.agents.models import Agent, WorkerAgent, SupervisorAgent
from agentcompose.agents.factory import AgentFactory
from agentcompose.agents.registry import AgentRegistry

__all__ = [
    "Agent",
    "WorkerAgent",
    "SupervisorAgent",
    "AgentFactory",
    "AgentRegistry",
]
