from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import ToolNode, tools_condition

from app.agents.state import AgentState
from app.agents.tools import search_documents
from app.llm.ollama_client import llm
from langgraph.checkpoint.memory import InMemorySaver

tools = [search_documents]

llm_with_tools = llm.bind_tools(tools)


def agent(state: AgentState):
    response = llm_with_tools.invoke(state["messages"])

    return {
        "messages": [response]
    }


builder = StateGraph(AgentState)

builder.add_node("agent", agent)
builder.add_node("tools", ToolNode(tools))

builder.add_edge(START, "agent")

builder.add_conditional_edges(
    "agent",
    tools_condition,
)

builder.add_edge("tools", "agent")

checkpointer = InMemorySaver()

agent_graph = builder.compile(
    checkpointer=checkpointer
)