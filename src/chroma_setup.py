import os
from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader, DirectoryLoader
from langchain_core.documents import Document

def setup_chroma():
    # Initialize the embedding model from Ollama
    embeddings = OllamaEmbeddings(model='nomic-embed-text')

    # Create or connect to a persistent ChromaDB
    vector_store = Chroma(
        collection_name="chat_collection",
        embedding_function=embeddings,
        persist_directory="./chroma_langchain_db",  # Where to save data locally, remove if not necessary
    )
    return vector_store

def load_documents(directory_path):
    loader = DirectoryLoader(directory_path,glob="**/*.txt",loader_cls=TextLoader)
    documents = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=200)
    chunks = text_splitter.split_documents(documents)
    return chunks

def add_documents_to_vectorstore(vectorstore,documents):
    vectorstore.add_documents(documents)
    vectorstore.persist()
    print(f"Added {len(documents)} document chunks to ChromaDB")

def main():
    vectorstore = setup_chroma()

    query = "What is a mile in kilometres?"
    results = vectorstore.similarity_search(query,k=2)

    print("Query Results:")
    for doc in results:
        print(f"Content:{doc.page_content[:100]}...")
        print(f"Source:{doc.metadata}")
        print("-"*50)


if __name__ == "__main__":
    main()