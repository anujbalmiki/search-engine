class InvertedIndex():

    def __init__(self):
        self.index = {}

    def add_index(self, doc_id, tokens):
        for token in tokens:
            if token not in self.index:
                self.index[token] = set()
            self.index[token].add(doc_id)

    def search(self, token):
        return self.index.get(token, set())