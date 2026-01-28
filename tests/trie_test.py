import sys
import os

# Ensure the project root is in the path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.trie import Trie

def test_trie():
    print("--- 1. Initializing Trie ---")
    trie = Trie()

    # Manual Ingestion
    words = ["python", "pytest", "pyramid", "data"]
    for word in words:
        trie.insert(word)
        print(f"Inserted: {word}")

    print("\n--- 2. Running Autocomplete Tests ---")

    # Test Case 1: Standard Prefix
    # Expected: ["pyramid", "pytest", "python"]
    res_py = trie.autocomplete("py", k=10)
    print(f"Search 'py': {res_py}")
    assert len(res_py) == 3, f"Expected 3 words, got {len(res_py)}"

    # Test Case 2: K-Limit
    # Expected: Any 2 from the py list (usually pyramid, pytest)
    res_k2 = trie.autocomplete("py", k=2)
    print(f"Search 'py' (k=2): {res_k2}")
    assert len(res_k2) == 2, f"Expected 2 words, got {len(res_k2)}"

    # Test Case 3: Single Result
    # Expected: ["data"]
    res_da = trie.autocomplete("da", k=5)
    print(f"Search 'da': {res_da}")
    assert res_da == ["data"], f"Expected ['data'], got {res_da}"

    # Test Case 4: Missing Prefix
    # Expected: []
    res_zz = trie.autocomplete("zz", k=5)
    print(f"Search 'zz': {res_zz}")
    assert res_zz == [], f"Expected [], got {res_zz}"

    print("\n✅ All Trie tests passed!")

if __name__ == "__main__":
    try:
        test_trie()
    except AssertionError as e:
        print(f"❌ Test Failed: {e}")
    except Exception as e:
        print(f"💥 An error occurred: {e}")