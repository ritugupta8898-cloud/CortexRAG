from langchain_ollama import ChatOllama
def generate_response(query,docs,model="gpt-4.1-mini"):
    llm = ChatOllama(
    model="llama3")

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )


    prompt = f"""
You are an expert AI research assistant.

Answer the user's question using the provided research context.

Rules:
- Write naturally and clearly
- Combine information from multiple retrieved chunks
- Be concise but technically accurate
- If the answer is not in the context, say so
- Do not hallucinate information

Context:
{context}

Question:
{query}

Answer:
"""
    response = llm.invoke(prompt)

    return response.content