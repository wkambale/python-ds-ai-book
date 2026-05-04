from dataclasses import dataclass
from typing import List, Optional

@dataclass
class EvalExample:
    """A single evaluation example for RAG testing."""
    question: str
    expected_answer: str
    relevant_chunks: List[str]  # Text snippets that should be retrieved

def evaluate_retrieval(
    examples: List[EvalExample],
    vector_store,
    k: int = 4
) -> dict:
    """
    Evaluate retrieval quality on a set of examples.
    """
    hits = 0
    total = len(examples)

    for example in examples:
        results = vector_store.similarity_search(example.question, k=k)
        retrieved_text = " ".join([doc.page_content for doc in results])
        for relevant in example.relevant_chunks:
            if relevant.lower() in retrieved_text.lower():
                hits += 1
                break

    return {
        "recall@k": hits / total,
        "k": k,
        "total_examples": total
    }