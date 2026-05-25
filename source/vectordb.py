from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

def vectordb(doc):
    vector_store = Chroma(
        embedding_function = HuggingFaceEmbeddings(
           model_name="BAAI/bge-small-en-v1.5"
           ),
        persist_directory = "/Users/pratyushgupta/Documents/rag/vector_store",
        collection_name = "research_papers"
    )
    vector_store.add_documents(doc)
    return

