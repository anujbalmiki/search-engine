import re
from tokenizer import tokenize

class NaiveSearch():

    def __init__(self, storage):
        self.storage_obj = storage
        self.tokenize = tokenize

    def search(self, keyword):
        if not isinstance(keyword, str) or not keyword.split():
            raise ValueError("Keyword must be a non-empty string")
        result = []
        cleaned_keyword = re.sub(r'[^\w\s]', '', keyword.lower())
        documents = self.storage_obj.get_all_documents()
        for key, text in documents.items():
            cleaned_text = self.tokenize(text)
            if cleaned_keyword in cleaned_text:
                result.append(key)
        return result


class IndexedSearch():

    def __init__(self, index):
        self.index_obj = index
        self.tokenize = tokenize

    def search(self, keyword):
        if not isinstance(keyword, str) or not keyword.split():
            raise ValueError("Keyword must be a non-empty string")
        result = []
        cleaned_keyword = self.tokenize(keyword)
        result = list(self.index_obj.search(cleaned_keyword[0]))
        return result