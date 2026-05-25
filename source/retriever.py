from source.query_expansion import expand_query

def retrieve(db, query: str):

    all_docs = []

    seen = set()

    initial_results = db.similarity_search_with_score(
        query,
        k=1
    )

    anchor_doc, initial_score = initial_results[0]

    if len(query.split()) <= 4 and initial_score < 0.35:

        anchor_context = anchor_doc.page_content

        queries = expand_query(
            query,
            anchor_context
        )

    else:

        queries = [query]

    for q in queries:

        results = db.similarity_search_with_score(
            q,
            k=4
        )

        for doc, score in results:

            if doc.page_content not in seen:
                print(score)

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