"""API route handlers."""

from agentweave.api.routes.chat import router as chat_router
from agentweave.api.routes.agents import router as agents_router
from agentweave.api.routes.health import router as health_router
from agentweave.api.routes.openai_compat import router as openai_router
from agentweave.api.routes.tasks import router as tasks_router
from agentweave.api.routes.langgraph_studio import router as langgraph_router
from agentweave.api.routes.conversations import router as conversations_router

__all__ = [
    "chat_router",
    "agents_router",
    "health_router",
    "openai_router",
    "tasks_router",
    "langgraph_router",
    "conversations_router",
]
