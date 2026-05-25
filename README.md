# CortexRAG

Production-style Retrieval-Augmented Generation (RAG) system for research papers featuring semantic search, query expansion, persistent vector storage, contextual retrieval, and local LLM-powered response generation using FastAPI, ChromaDB, and HuggingFace embeddings.

Focused heavily on retrieval quality, semantic search behavior, grounding reliability, and retrieval debugging workflows for research-oriented RAG systems.

---

## Demo

### API Response Example

![CortexRAG Demo](assets/image.png)

---

## Features

- Research paper ingestion pipeline
- Semantic vector search using ChromaDB
- HuggingFace embedding models
- Multi-query retrieval system
- Context-aware query expansion using local LLMs
- Retrieval metadata with source tracking
- FastAPI backend for API serving
- Local LLM inference using Ollama
- Persistent vector database storage

---

## Architecture

```text
User Query
↓
Query Expansion
↓
Semantic Retrieval
↓
Context Aggregation & Deduplication
↓
Grounded LLM Response Generation
↓
FastAPI API Response
```

---

## Tech Stack

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

## Project Structure

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

---
## Retrieval Evaluation

CortexRAG includes a lightweight retrieval evaluation framework for benchmarking semantic retrieval quality across technical research queries.

### Current Benchmark Results

| Metric | Score |
|---|---|
| Top-1 Retrieval Accuracy | 75% |
| Top-3 Coverage Accuracy | 75% |
| Average Retrieval Score | 0.5679 |
| Total Indexed Chunks | 2320 |

## Chunking Strategy Experiments

Different chunking configurations were evaluated using the retrieval benchmark framework.

| Chunk Size | Overlap | Top-1 Accuracy | Top-3 Coverage | Avg Retrieval Score |
|---|---|---|---|---|
| 400 | 80 | 75% | 75% | 0.5679 |
| 550 | 90 | 100% | 100% | 0.5714 |
| 600 | 100 | 100% | 100% | 0.5396 |
| 700 | 120 | 100% | 100% | 0.5981 |

### Key Findings

- Larger chunks improved comparison-query retrieval performance
- Smaller chunks improved specificity but occasionally reduced retrieval coverage
- Excessively large chunks introduced semantic retrieval noise
- 600/100 produced the best balance between semantic precision and contextual completeness
- Chunking strategy had a measurable impact on retrieval grounding quality

### Evaluation Queries

| Query | Expected Sources |
|---|---|
| What is LoRA? | lora.pdf |
| What is BERT? | bert.pdf |
| Differentiate between LoRA and BERT? | lora.pdf, bert.pdf |
| What is GPT-3? | gpt3.pdf |

### Key Observations

- Multi-query semantic retrieval improved retrieval coverage for technical queries
- Smaller chunk sizes improved retrieval specificity but occasionally reduced contextual completeness
- Comparison-style queries were significantly harder than single-concept retrieval
- Query expansion improved grounding for abbreviation-heavy queries such as “LoRA”
- Retrieval debugging exposed semantic drift and noisy neighbor issues during experimentation

### Evaluation Framework

The evaluation pipeline benchmarks:

- Top-1 retrieval accuracy
- Top-3 retrieval coverage
- Average retrieval similarity score
- Multi-document retrieval behavior

The framework was used to compare:
- chunking strategies
- overlap sizes
- query expansion behavior
- retrieval filtering logic


## Key Engineering Challenges

- Preventing semantic drift during query expansion
- Reducing noisy retrieval from vector similarity search
- Balancing chunk size vs retrieval precision
- Improving grounding quality for local LLM generation
- Handling short technical queries with abbreviation-heavy terminology

---

## Retrieval Engineering Learnings

During development, multiple retrieval-quality issues emerged that required iterative experimentation and debugging.

Key observations and improvements included:

- Query expansion occasionally caused semantic drift and hallucinated technical terminology
- Multi-query retrieval introduced duplicate and low-relevance chunks
- Retrieval quality varied significantly with chunk size and overlap tuning
- Short technical queries (e.g., “What is LoRA?”) required different handling compared to descriptive queries
- Context-assisted query expansion was explored for abbreviation-heavy retrieval
- Context filtering and deduplication logic were refined to improve grounding quality
- Grounded generation prompts were added to reduce hallucinations from the local LLM
- Retrieval scores and chunk previews were exposed through the API for debugging and observability

These experiments helped improve understanding of:

- Semantic vector search behavior
- Embedding similarity limitations
- Retrieval ranking instability
- Query expansion tradeoffs
- Grounding vs hallucination dynamics in RAG systems

---
## Failure Cases

Observed retrieval failure modes included:

- semantic drift during query expansion
- noisy retrieval from large chunks
- abbreviation ambiguity in technical queries
- context dilution from excessive chunk overlap
## Setup

### Clone Repository

```bash
git clone https://github.com/ritugupta8898-cloud/CortexRAG.git
cd CortexRAG
```

### Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Ingestion

```bash
python3 ingest.py
```

### Start Backend

```bash
uvicorn backend.app:app --reload
```

---

## API Endpoint

### Chat Endpoint

```bash
GET /chat?query=your_query
```

Example:

```bash
http://127.0.0.1:8000/chat?query=What is LoRA?
```

---

## Example Retrieval Metadata

The API exposes:

- Retrieved source documents
- Similarity scores
- Chunk previews

to help analyze retrieval quality and grounding behavior.

---

## Future Improvements

- Hybrid Retrieval
- Cross-Encoder Reranking
- Metadata Filtering
- Conversational Memory
- Frontend UI
- Streaming Responses
- Evaluation Metrics

---

## Example Use Cases

- Research paper semantic search
- AI research assistant
- Knowledge retrieval systems
- Context-aware QA systems
- NLP experimentation
- Retrieval engineering experimentation
```