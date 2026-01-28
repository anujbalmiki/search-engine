# Text search engine built from scratch to learn DSA

### Document Handling
- Documents are plain text
- Stored in memory only
- Each Document gets a numeric ID starting from 1

### Tokenization Rules
- Convert text to lowercase
- Remove punctuation
- Split by whitespace

**Examples:**

| Raw Input Sentence | Expected Output Tokens |
| :--- | :--- |
| "The quick brown fox jumps!" | `['the', 'quick', 'brown', 'fox', 'jumps']` |
| "Hello, world? Is anyone there?" | `['hello', 'world', 'is', 'anyone', 'there']` |
| "Data science is 100% awesome." | `['data', 'science', 'is', '100', 'awesome']` |
| "Wait... did he say 'yes'?" | `['wait', 'did', 'he', 'say', 'yes']` |
| "It's a beautiful day in NYC." | `['its', 'a', 'beautiful', 'day', 'in', 'nyc']` |

### Inverted Index
- Index maps word → document IDs
- Document insertion updates the index immediately

**Example Index:**

| Word | Document IDs |
| :--- | :--- |
| the | [1, 2] |
| cat | [1] |
| sat | [1, 2] |
| dog | [2] |


### Phase 1 complete: 
- storage
- tokenizer 
- inverted 
- index 
- naive and indexed search

### Phase 2 complete:
- multi-word 
- AND/OR queries using set intersection and union.

### Phase 3 complete: 
- relevance scoring
- top-K retrieval
- heap-based ranking.

### Phase 4 complete:
- autocomplete implemented
- trie-based
- DFS Traversal