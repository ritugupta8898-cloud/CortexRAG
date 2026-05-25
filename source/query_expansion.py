from langchain_ollama import ChatOllama


llm = ChatOllama(
    model="llama3"
)
def expand_query(query:str):
    prompt = f"""
You are an expert query expansion system for research paper retrieval.

Generate 3 to 5 highly effective semantic search queries.

Rules:
- Focus on technical meaning
- Include related terminology
- Break comparisons into subtopics
- Keep each query concise
- Queries should help retrieve research paper chunks
- Return ONLY the queries
- One query per line
- No numbering
- No explanations

User Query:
{query}
"""

    response = llm.invoke(prompt)
    queries = response.content.split("\n")

    queries = [
        q.strip()
        for q in queries
        if q.strip()
    ]

    return queries