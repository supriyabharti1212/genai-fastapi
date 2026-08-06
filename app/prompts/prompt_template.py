from langchain_core.prompts import ChatPromptTemplate

chat_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are a Senior Python Mentor.

Rules:
- Explain in simple English.
- Give one real-life example.
- Keep the answer under 150 words.
- If the user asks for code, provide clean code.
"""
        ),
        (
            "human",
            "{question}"
        )
    ]
)