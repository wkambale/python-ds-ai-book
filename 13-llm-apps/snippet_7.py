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

    "What are my rights if I am arrested?",
    vector_store
)