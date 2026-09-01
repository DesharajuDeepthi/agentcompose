"""A2A integration module for AgentWeave."""

from agentweave.a2a.models import (
    AgentCard,
    AgentSkill,
    AgentCapabilities,
    DiscoveredAgent,
    A2AMessage,
    A2ARequest,
    A2AResponse,
    TaskStatus,
)
from agentweave.a2a.discovery import A2ADiscovery
from agentweave.a2a.client import A2AClient

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
