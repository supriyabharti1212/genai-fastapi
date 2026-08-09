


from langgraph.graph import StateGraph, START, END

from app.agents.state import AgentState
from app.agents.tools import search_documents
from app.llm.ollama_client import llm


def retrieve_context(state: AgentState):
    context = search_documents(state["question"])

    return {
        "context": context
    }


def generate_answer(state: AgentState):
    prompt = f"""
You are a question-answering assistant.

Use ONLY the information provided in the context below.

If the answer is not present in the context, say:
"I don't have enough information in the provided context."

Context:
{state["context"]}

Question:
{state["question"]}

Answer:
"""

    response = llm.invoke(prompt)

    return {
        "answer": response.content
    }


graph_builder = StateGraph(AgentState)

graph_builder.add_node("retrieve", retrieve_context)
graph_builder.add_node("generate", generate_answer)

graph_builder.add_edge(START, "retrieve")
graph_builder.add_edge("retrieve", "generate")
graph_builder.add_edge("generate", END)

agent_graph = graph_builder.compile()