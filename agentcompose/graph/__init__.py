"""LangGraph orchestration module for AgentCompose.

This module provides the graph building and state management using:
- LangGraph StateGraph for workflow orchestration
- LangChain chat models for LLM integration
- create_react_agent for tool-using workers

Usage:
    from agentcompose.graph import GraphFactory, GraphState

    factory = GraphFactory(config, agent_registry, llm_factory, tool_registry)
    graph = factory.compile(checkpointer=checkpointer)

    result = await graph.ainvoke(initial_state, config={"configurable": {"thread_id": "..."}})
"""

from agentcompose.graph.state import (
    GraphState,
    WorkerResult,
    ResultOutput,
    ResultType,
    create_initial_state,
)
from agentcompose.graph.factory import GraphFactory

__all__ = [
    "GraphState",
    "WorkerResult",
    "ResultOutput",
    "ResultType",
    "create_initial_state",
    "GraphFactory",
]
