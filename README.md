# CortexRAG

Production-style Retrieval-Augmented Generation (RAG) system for research papers featuring semantic search, query expansion, persistent vector storage, contextual retrieval, and local LLM-powered response generation using FastAPI, ChromaDB, and HuggingFace embeddings.

---

# Features

- Research paper ingestion pipeline
- Semantic vector search using ChromaDB
- HuggingFace embedding models
- Multi-query retrieval system
- Query expansion using local LLMs
- Retrieval metadata with source tracking
- FastAPI backend for API serving
- Local LLM inference using Ollama
- Persistent vector database storage

---

# Architecture

User Query
↓
Query Expansion
↓
Semantic Retrieval
↓
Context Aggregation
↓
LLM Response Generation
↓
FastAPI API Response

---

# Tech Stack

- Python
- FastAPI
- ChromaDB
- LangChain
- HuggingFace Embeddings
- Ollama
- Llama3
- Semantic Search
- Vector Databases

---

# Project Structure

```bash
backend/
    app.py

source/
    dataloader.py
    splitter.py
    vectordb.py
    retriever.py
    query_expansion.py
    rag_chain.py

data/
    research papers

vector_store/
    persisted embeddings

ingest.py
```

# Setup

## Clone Repository

```bash
git clone https://github.com/ritugupta8898-cloud/CortexRAG.git
cd CortexRAG
```

## Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run Ingestion

```bash
python3 ingest.py
```

## Start Backend

```bash
uvicorn backend.app:app --reload
```

---

# API Endpoint

## Chat Endpoint

```bash
GET /chat?query=your_query
```

Example:

```bash
http://127.0.0.1:8000/chat?query=(your question)
```

---

# Future Improvements

- Hybrid Retrieval
- Reranking
- Metadata Filtering
- Conversational Memory
- Frontend UI
- Streaming Responses
- Evaluation Metrics

---

# Example Use Cases

- Research paper semantic search
- AI research assistant
- Knowledge retrieval systems
- Context-aware QA systems
- NLP experimentation
