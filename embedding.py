import os
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import DocArrayInMemorySearch
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from dotenv import load_dotenv
from xml_parser import parse_xml_files

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def create_documents_from_recall_data(recall_data):
    """
    Convert all recall data into a single LangChain document for embedding.
    """
    text = "\n\n".join([
        f"Brand: {entry['brand']}\n"
        f"Company: {entry['company']}\n"
        f"Date: {entry['date']}\n"
        f"Product Description: {entry['product_description']}\n"
        f"Reason: {entry['reason']}\n"
        f"URL: {entry['url']}"
        for entry in recall_data
    ])
    
    metadata = {"source": "combined_data"}
    
    return [Document(page_content=text, metadata=metadata)]


def create_vector_store(documents, embeddings):
    """Create an in-memory vector store with proper text splitting."""
    return DocArrayInMemorySearch.from_documents(
        documents=documents,
        embedding=embeddings
    )

def embed_database(data_path):
    """Embed the XML database and return the vector store."""
    embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)

    recall_data = parse_xml_files(data_path)

    documents = create_documents_from_recall_data(recall_data)

    vector_store = create_vector_store(documents, embeddings)
    print("Database embedded successfully.")
    return vector_store

if __name__ == "__main__":
    vector_store = embed_database("./data")