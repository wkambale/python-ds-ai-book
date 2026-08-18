from typing import List
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document

def load_and_split_pdf(file_path: str, chunk_size: int = 500, chunk_overlap: int = 50) -> List[Document]:
    """
    Load a PDF file and return list of page documents split into chunks.

    Args:
        file_path: Path to PDF file
        chunk_size: Size of text chunks
        chunk_overlap: Overlap between text chunks

    Returns:
        List of Document objects
    """
    loader = PyPDFLoader(file_path)
    documents = loader.load()
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )
    return splitter.split_documents(documents)