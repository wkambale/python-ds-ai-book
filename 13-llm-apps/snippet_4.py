from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document

    """
    Load a PDF file and return list of page documents.

    Args:
        file_path: Path to PDF file

    Returns:
        List of Document objects, one per page
    """
    )