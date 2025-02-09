import os
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import DocArrayInMemorySearch
from langchain_core.documents import Document
from dotenv import load_dotenv
from xml_parser import parse_xml_files
import sys

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Similarity threshold (adjustable)
SIMILARITY_THRESHOLD = 0.7  # Adjust this as needed

def create_documents_from_recall_data(recall_data):
    """Convert recall data into LangChain documents for embedding."""
    documents = []
    for entry in recall_data:
        text = (
            f"Brand: {entry['brand']}\n"
            f"Company: {entry['company']}\n"
            f"Date: {entry['date']}\n"
            f"Product Description: {entry['product_description']}\n"
            f"Reason: {entry['reason']}\n"
            f"URL: {entry['url']}"
        )
        metadata = {
            "brand": entry["brand"],
            "company": entry["company"],
            "date": entry["date"],
            "url": entry["url"]
        }
        documents.append(Document(page_content=text, metadata=metadata))
    return documents

def create_vector_store(documents, embeddings):
    """Create an in-memory vector store."""
    return DocArrayInMemorySearch.from_documents(documents=documents, embedding=embeddings)

def embed_database(data_path):
    """Embed the XML database and return the vector store."""
    embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
    recall_data = parse_xml_files(data_path)
    documents = create_documents_from_recall_data(recall_data)
    return create_vector_store(documents, embeddings)

def search_recall_data(vector_store, query, top_k=50):
    """Retrieve recall data from vector store with a similarity threshold."""
    retriever = vector_store.as_retriever(search_kwargs={"k": top_k})
    results = retriever.get_relevant_documents(query, score=True)  # Get scores
    
    if not results:
        return "No relevant recall data found."

    # Filter results based on the similarity threshold
    filtered_results = [(doc, score) for doc, score in results if score >= SIMILARITY_THRESHOLD]

    if not filtered_results:
        return "No results meet the similarity threshold."

    output = "**Recall Search Results:**\n\n"
    for doc, score in filtered_results:
        output += f"- **Brand:** {doc.metadata['brand']}\n"
        output += f"- **Company:** {doc.metadata['company']}\n"
        output += f"- **Date:** {doc.metadata['date']}\n"
        output += f"- **URL:** {doc.metadata['url']}\n"
        output += f"- **Similarity Score:** {score:.2f}\n"
        output += f"- **Details:** {doc.page_content}\n\n"

    return output

if __name__ == "__main__":
    vector_store = embed_database("./data")
    query = "Find recalls related to defective products."
    response = search_recall_data(vector_store, query)
    
    sys.stdout.reconfigure(encoding='utf-8')
    print(response)
