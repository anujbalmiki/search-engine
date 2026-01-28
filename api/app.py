import sys
import os
import time  # Import time module

# This adds the project root to the path 
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from storage.document_store import Storage
from core.tokenizer import tokenize
from core.index import InvertedIndex
from core.search import NaiveSearch, IndexedSearch
from core.trie import Trie

def run_test():
    # 1. Setup Instances
    store = Storage()
    index = InvertedIndex()
    trie = Trie()

    # 2. Data Ingestion
    documents = [
        "The quick brown fox",
        "The lazy dog jumps over the fox",
        "Python is the great for search engines, python, python",
        "Data structures are fun"
    ]

    print("--- Ingesting Documents ---")
    for text in documents:
        doc_id = store.add_document(text)
        tokens = tokenize(text)
        index.add_index(doc_id, tokens)
        
        # insert the token in the trie
        for token in tokens:
            trie.insert(token)
        print(f"Added ID {doc_id}: '{tokens}'")

    # 3. Initialize Searchers
    naive_searcher = NaiveSearch(store)
    indexed_searcher = IndexedSearch(index, store)

    # 4. Run Tests
    test_keywords = ["fox", "the or python", "missingword or brown"]

    print("\n--- Running Comparisons & Performance ---")
    for word in test_keywords:
        # Measure Naive Search Time
        start_naive = time.perf_counter()
        naive_results = naive_searcher.search(word)
        end_naive = time.perf_counter()
        naive_time = (end_naive - start_naive) * 1000 # convert to ms

        # Measure Indexed Search Time
        start_indexed = time.perf_counter()
        indexed_results = indexed_searcher.search(word)
        end_indexed = time.perf_counter()
        indexed_time = (end_indexed - start_indexed) * 1000 # convert to ms

        print(f"Keyword: '{word}'")
        print(f"  Naive Results:   {naive_results} ({naive_time:.4f} ms)")
        print(f"  Indexed Results: {indexed_results} ({indexed_time:.4f} ms)")
        
        if set(naive_results) == set(indexed_results):
            print("  ✅ Match!")
        else:
            print("  ❌ MISMATCH found!")
        print("-" * 30)

if __name__ == "__main__":
    run_test()