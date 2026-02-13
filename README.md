# 🧠 Text Search Engine Built from Scratch

This project is a search engine backend implemented completely from scratch to learn **Data Structures & Algorithms in a real system**.

It supports:

- 🔎 Keyword search  
- 🔗 Multi-word boolean queries (AND / OR)  
- 📊 Relevance ranking (Top-K results using heap)  
- 🌳 Autocomplete (Trie / Prefix Tree)  
- ✏️ Fuzzy search (typo tolerance using Edit Distance + Dynamic Programming)

No external search libraries are used. Everything is implemented manually.

---

# 📦 How the System Works

High-level flow:

```
Raw Text
   ↓
Tokenizer
   ↓
Inverted Index + Trie
   ↓
Search Layer (Boolean + Ranking + Fuzzy)
```

Each component has a single responsibility and is independently testable.

---

# 📝 Document Handling

- Documents are plain text
- Stored in memory
- Each document receives a numeric ID (starting from 1)
- Document ingestion updates:
  - Inverted Index
  - Trie (for autocomplete)

---

# 🔤 Tokenization Rules

All text is normalized using consistent rules:

- Convert to lowercase  
- Remove punctuation  
- Split by whitespace  

### Examples

| Raw Input | Tokens |
|------------|--------|
| "The quick brown fox jumps!" | `['the', 'quick', 'brown', 'fox', 'jumps']` |
| "Hello, world? Is anyone there?" | `['hello', 'world', 'is', 'anyone', 'there']` |
| "Data science is 100% awesome." | `['data', 'science', 'is', '100', 'awesome']` |
| "It's a beautiful day in NYC." | `['its', 'a', 'beautiful', 'day', 'in', 'nyc']` |

Tokenizer is the single source of truth for text normalization.

---

# 📚 Inverted Index

Core structure:

```
token → set of document IDs
```

Example:

| Word | Document IDs |
|------|---------------|
| the  | [1, 2] |
| cat  | [1] |
| sat  | [1, 2] |
| dog  | [2] |

This allows fast lookup without scanning all documents.

---

# 🚀 Project Phases

The system was built step-by-step to progressively introduce DSA concepts.

---

## ✅ Phase 1 — Core Search Engine

Implemented:

- In-memory document storage  
- Tokenizer  
- Inverted index  
- Naive linear search  
- Indexed search  

Goal: Understand indexing vs scanning.

Concepts used:
- Hash maps  
- Sets  
- Time complexity comparison  

---

## ✅ Phase 2 — Boolean Queries (AND / OR)

Added support for:

- Multi-word queries  
- AND logic (default)  
- OR logic (explicit using "or")  

Examples:

```
python search
python OR data
```

Concepts used:
- Set intersection  
- Set union  
- Query parsing  

---

## ✅ Phase 3 — Relevance Ranking & Top-K

Added ranking using **Term Frequency (TF)**.

- Score = number of query token occurrences in document  
- Results returned in ranked order  
- Top-K implemented using a min-heap  
- Avoids full sorting  

Concepts used:
- Heaps (priority queues)  
- Top-K optimization  

---

## ✅ Phase 4 — Autocomplete (Trie)

Implemented prefix-based autocomplete using a **Trie (Prefix Tree)**.

Features:

- Character-level tree  
- DFS traversal  
- Alphabetical suggestions  
- Optional limit (`k`)  

Example:

```
py → python, pytest, pyramid
```

Concepts used:
- Trees  
- DFS  
- Prefix optimization  

---

## ✅ Phase 5 — Fuzzy Search (Edit Distance + DP)

Added typo tolerance using **Levenshtein Edit Distance**.

Behavior:

- If exact search returns no results  
- System finds similar tokens within a distance threshold  
- Boolean logic preserved  
- Ranking still applied  

Examples:

```
pythn → python
srch  → search
```

Concepts used:
- Dynamic Programming  
- State transition tables  
- Algorithmic fallback strategies  

---

# 🏗 Current Architecture

```
Storage        → owns documents
Tokenizer      → text → tokens
InvertedIndex  → token → doc_ids
Trie           → token prefixes → tokens
Search Layer   → AND / OR / ranking / fuzzy fallback
```

Each layer:

- Has a single responsibility  
- Is independently testable  
- Avoids mixing concerns  

---

# 🧠 DSA Concepts Covered

This project demonstrates practical usage of:

- Hash Maps  
- Sets  
- Trees (Trie)  
- DFS  
- Heaps  
- Dynamic Programming  
- Boolean logic processing  
- Performance optimization  

This is DSA applied inside a working system, not isolated exercises.

---

# 🎯 Purpose

The goal of this project is to:

- Learn DSA by building real systems  
- Understand how search engines work internally  
- Connect algorithmic thinking with backend design  
- Build a strong, interview-ready project  
