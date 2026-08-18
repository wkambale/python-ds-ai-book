from typing import List
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.schema import Document

def create_vector_store(
    chunks: List[Document],
    embedding_model_name: str = "sentence-transformers/all-MiniLM-L6-v2",
    persist_directory: str = "./chroma_db"
) -> Chroma:
    """
    Create a vector store from document chunks.

    Args:
        chunks: List of document chunks to store
        embedding_model_name: Model identifier for generating embeddings
        persist_directory: Directory to persist the vector store
    """
    embeddings = HuggingFaceEmbeddings(model_name=embedding_model_name)
    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=persist_directory
    )
    return vector_store