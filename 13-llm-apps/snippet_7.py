from typing import List
from langchain.schema import Document

def build_rag_prompt(
    query: str,
    retrieved_docs: List[Document],
    system_context: str = ""
) -> str:
    """
    Construct a RAG prompt with retrieved context.

    Args:
        query: User's question
        retrieved_docs: Relevant document chunks
        system_context: Additional system instructions

    Returns:
        Complete prompt string
    """
    context = "\n\n".join([doc.page_content for doc in retrieved_docs])
    prompt = f"""Context:
{context}

System Instructions:
{system_context}

Question: {query}
Answer:"""
    return prompt