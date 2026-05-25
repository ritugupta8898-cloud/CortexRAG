from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

from source.retriever import retrieve


db = Chroma(
    persist_directory="/Users/pratyushgupta/Documents/rag/vector_store",
    embedding_function=HuggingFaceEmbeddings(
        model_name="BAAI/bge-small-en-v1.5"
    ),
    collection_name="research_papers"
)


print(f"Total Chunks in DB: {db._collection.count()}")


test_queries = [

    {
        "query": "What is LoRA?",
        "expected_sources": [
            "lora.pdf"
        ]
    },

    {
        "query": "What is BERT?",
        "expected_sources": [
            "bert.pdf"
        ]
    },

    {
        "query": "Differentiate between LoRA and BERT?",
        "expected_sources": [
            "lora.pdf",
            "bert.pdf"
        ]
    },

    {
        "query": "What is GPT-3?",
        "expected_sources": [
            "gpt3.pdf"
        ]
    }

]


top1_correct = 0
top3_correct = 0

all_scores = []

total = len(test_queries)


print("\n==============================")
print("Running Retrieval Evaluation")
print("==============================\n")


for test in test_queries:

    query = test["query"]

    expected_sources = test["expected_sources"]

    results = retrieve(
        db,
        query
    )

    retrieved_sources = [
        item["source"]
        for item in results
    ]

    retrieved_scores = [
        item["score"]
        for item in results
    ]


    print(f"\nQuery: {query}")

    print(f"Expected Sources: {expected_sources}")

    print("\nRetrieved Sources:")

    for source in retrieved_sources[:5]:
        print(f" - {source}")


    # Top-1 Accuracy
    if len(retrieved_sources) > 0:

        if retrieved_sources[0] in expected_sources:
            top1_correct += 1


    # Top-3 Coverage Accuracy
    top3 = retrieved_sources[:3]

    if all(
        source in top3
        for source in expected_sources
    ):
        top3_correct += 1


    # Average score tracking
    if len(retrieved_scores) > 0:
        all_scores.extend(retrieved_scores)


top1_accuracy = (top1_correct / total) * 100

top3_accuracy = (top3_correct / total) * 100

average_score = sum(all_scores) / len(all_scores)


print("\n==============================")
print("Evaluation Results")
print("==============================")

print(f"Top-1 Accuracy: {top1_accuracy:.2f}%")

print(f"Top-3 Coverage Accuracy: {top3_accuracy:.2f}%")

print(f"Average Retrieval Score: {average_score:.4f}")

print("==============================\n")