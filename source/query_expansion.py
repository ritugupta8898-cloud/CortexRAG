from langchain_ollama import ChatOllama


llm = ChatOllama(
    model="llama3"
)
def expand_query(query:str, anchor_context=None):
   



    prompt = f"""
You are a retrieval query expansion system.

Original Query:
{query}

Relevant Context:
{anchor_context}

Generate 3 semantic search queries.

Rules:
- Preserve technical terminology
- Use the context to disambiguate abbreviations
- Never invent meanings
- Keep queries concise
- Return only queries
"""

    response = llm.invoke(prompt)
    queries = response.content.split("\n")

    queries = [
        q.strip()
        for q in queries
        if q.strip()
    ]
    
    return queries