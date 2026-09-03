"""A2A integration module for AgentCompose."""

from agentcompose.a2a.models import (
    AgentCard,
    AgentSkill,
    AgentCapabilities,
    DiscoveredAgent,
    A2AMessage,
    A2ARequest,
    A2AResponse,
    TaskStatus,
)
from agentcompose.a2a.discovery import A2ADiscovery
from agentcompose.a2a.client import A2AClient

__all__ = [
    "AgentCard",
    "AgentSkill",
    "AgentCapabilities",
    "DiscoveredAgent",
    "A2AMessage",
    "A2ARequest",
    "A2AResponse",
    "TaskStatus",
    "A2ADiscovery",
    "A2AClient",
]
