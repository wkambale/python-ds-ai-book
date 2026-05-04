from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

    chunks: List[Document],
    embedding_model_name: str = "sentence-transformers/all-MiniLM-L6-v2",
    persist_directory: str = "./chroma_db"
) -> Chroma:
    """
    Create a vector store from document chunks.

    Args:
    )