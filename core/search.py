import re
from .tokenizer import tokenize

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

    def search(self, search_text):
        if not isinstance(search_text, str) or not search_text.split():
            raise ValueError("Keyword must be a non-empty string")
        result = []
        operator = 'AND'

        if " or " in search_text.lower():
            operator = 'OR'
            search_text = search_text.replace(" or ", " ")

        tokens = self.tokenize(search_text)
        
        for token in tokens:
            result.append(self.index_obj.search(token))

        if len(result) >= 1:
            final_result = set.intersection(*result) if operator == 'AND' else set.union(*result)
        else:
            final_result = set(result)

        return final_result