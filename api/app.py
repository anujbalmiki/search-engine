import sys
import os
import time

# This adds the project root to the path 
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from storage.document_store import Storage
from core.tokenizer import tokenize
from core.index import InvertedIndex
from core.search import IndexedSearch
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
        
        # Insert tokens into Trie for autocomplete
        for token in tokens:
            trie.insert(token)
        print(f"Added ID {doc_id}: '{text}'")

    # 3. Initialize Searcher (No Naive Searcher needed anymore)
    indexed_searcher = IndexedSearch(index, store)

    # 4. Run Tests
    test_keywords = ["pythn fox", "the or python", "missingword or brown"]

    print("\n--- Running Indexed Search Results ---")
    for word in test_keywords:
        # Measure Indexed Search Time
        start_indexed = time.perf_counter()
        indexed_results = indexed_searcher.search(word, k=3)
        end_indexed = time.perf_counter()
        indexed_time = (end_indexed - start_indexed) * 1000 

        print(f"Keyword: '{word}' ({indexed_time:.4f} ms)")
        
        if not indexed_results:
            print("  Result: []")
        else:
            # We display the ID, the Score, and the actual Text from Storage
            for doc_id, score in indexed_results:
                content = store.get_document(doc_id)
                print(f"  ID: {doc_id} | Score: {score} | Content: '{content}'")
        
        print("-" * 30)

    # 5. Quick Autocomplete Test
    print("\n--- Autocomplete Test ---")
    print(f"Prefix 'py': {trie.autocomplete('py', k=2)}")

if __name__ == "__main__":
    run_test()