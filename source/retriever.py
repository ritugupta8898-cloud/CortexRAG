from source.query_expansion import expand_query

def retrieve(db, query: str):

    queries =  expand_query(query)

    all_docs = []

    seen = set()
    

    for q in queries:

        results = db.similarity_search_with_score(
            q,
            k=4
        )
        

        for doc, score in results:

            if doc.page_content not in seen:

                all_docs.append({
                    "document": doc,
                    "score": score,
                    "source": doc.metadata["paper_name"]
                })

                seen.add(doc.page_content)

    all_docs.sort(
        key=lambda x: x["score"]
    )

    return all_docs