from icecream import ic

def edit_distance(word1, word2):
    rows = len(word1) + 1
    cols = len(word2) + 1

    # Initialize the matrix with base cases (transforming to/from empty string)
    dist = [[0 for _ in range(cols)] for _ in range(rows)]

    for i in range(1, rows): dist[i][0] = i
    for j in range(1, cols): dist[0][j] = j

    for i in range(1, rows):
        for j in range(1, cols):
            if word1[i-1] == word2[j-1]:
                dist[i][j] = dist[i-1][j-1] # No cost if chars match
            else:
                dist[i][j] = 1 + min(
                    dist[i-1][j],    # Deletion
                    dist[i][j-1],    # Insertion
                    dist[i-1][j-1]   # Replacement
                )
    
    return dist[-1][-1]

def find_similar_tokens(target, vocabulary, max_distance=2):
    """
    vocabulary: a list or set of all unique tokens in the engine
    """
    matches = []
    for token in vocabulary:
        if abs(len(target) - len(token)) > max_distance:
            continue
        distance = edit_distance(target, token)
        if distance <= max_distance:
            matches.append(token)
    return matches

if __name__ == "__main__":
    vocabulary = ["python", "pyhon"]
    ic(find_similar_tokens("pythn", vocabulary)) # Returns ['python'] because the cost is 1