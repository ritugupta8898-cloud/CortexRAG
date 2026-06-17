from fastapi import FastAPI

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

from source.query_expansion import expand_query
from source.rag_chain import generate_response
from source.retriever import retrieve


app = FastAPI()


db = Chroma(
    persist_directory="/Users/pratyushgupta/Documents/rag/vector_store",
    embedding_function=HuggingFaceEmbeddings(
        model_name="BAAI/bge-small-en-v1.5"
    ),
    collection_name="research_papers"
)


@app.get("/chat")
def get_response(query: str):
    query = sanitize_input(query)

    retrieved_docs = retrieve(
        db,
        query
    )
    
    docs = [
        item["document"]
        for item in retrieved_docs
    ]

    response = generate_response(
        query,
        docs
    )

    return {
        "response": response,
        "retrieved_context": [
            {
                "source": item["source"],
                "score": item["score"],
                "preview": item["document"].page_content[:300]
            }
            for item in retrieved_docs
        ]
    }