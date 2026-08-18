from typing import List
from langchain.schema import Document
from langchain_community.vectorstores import Chroma

def retrieve_relevant_chunks(
    query: str,
    vector_store: Chroma,
    k: int = 4
) -> List[Document]:
    """
    Retrieve the most relevant document chunks for a query.

    Args:
        query: User's question in natural language
        vector_store: Chroma vector store to search
        k: Number of chunks to retrieve
    """
    return vector_store.similarity_search(query, k=k)