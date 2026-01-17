class Storage:
    def __init__(self):
        self.documents = {}
        self.next_id = 1

    def add_document(self, text):
        if not isinstance(text, str) or not text.strip():
            raise ValueError("Document must be a non-empty string")
        doc_id = self.next_id
        self.documents[doc_id] = text
        self.next_id += 1
        return doc_id

    def get_document(self, doc_id):
        if not isinstance(doc_id, int) or doc_id < 1:
            raise ValueError("Document ID must be a number geater than 0")
        return self.documents.get(doc_id)

    def get_all_documents(self):
        return self.documents.copy()
