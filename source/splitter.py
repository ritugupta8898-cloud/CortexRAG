from langchain_text_splitters import RecursiveCharacterTextSplitter

def clean_chunks(chunks):

    blocked_words = [
        "references",
        "bibliography",
        "acknowledgement",
        "acknowledgments",
        "appendix",
        "works cited"
    ]

    filtered_chunks = []

    for chunk in chunks:

        text = chunk.page_content.lower()

        if any(word in text for word in blocked_words):
            continue
        if text.count(",") > 18:
            continue
        filtered_chunks.append(chunk)

    return filtered_chunks

def text_split(docs, chunk_size=500, chunk_overlap=90):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )

    chunks = splitter.split_documents(docs)

    return chunks