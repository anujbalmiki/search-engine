from .tokenizer import tokenize

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.tokenize = tokenize

    def insert(self, token):
        node = self.root

        for char in token:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True

    def autocomplete(self, prefix, k):
        prefix_tokens = self.tokenize(prefix)
        if not prefix_tokens:
            return []

        target_prefix = prefix_tokens[0]
        node = self.root

        for char in target_prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        results = []
        self._dfs(node, target_prefix, results, k)
        return results
        
    def _dfs(self, node, current_word, results, k):
        if k is not None and len(results) >= k:
            return

        if node.is_end:
            results.append(current_word)

        for char in sorted(node.children.keys()):
            if k is not None and len(results) >= k:
                break
            self._dfs(node.children[char], current_word + char, results, k)