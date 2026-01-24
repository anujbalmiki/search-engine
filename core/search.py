import re
from .tokenizer import tokenize
from heapq import heappush, heappop

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

    def __init__(self, index, storage):
        self.index_obj = index
        self.storage_obj = storage
        self.tokenize = tokenize

    def search(self, search_text, k=None):
        if not isinstance(search_text, str) or not search_text.split():
            raise ValueError("Keyword must be a non-empty string")
        result = []
        operator = 'AND'

        if " or " in search_text.lower():
            operator = 'OR'
            search_text = search_text.replace(" or ", " ")

        search_tokens = self.tokenize(search_text)
        
        for token in search_tokens:
            result.append(self.index_obj.search(token))

        if len(result) >= 1:
            candidates = set.intersection(*result) if operator == 'AND' else set.union(*result)
        else:
            candidates = set(result)
        
        final_result = {}
        heap = []
        search_tokens = set(search_tokens)
        # Get the text, tokenize and count occurrences for each candidate
        for candidate in candidates:
            text = self.storage_obj.get_document(candidate)
            text_tokens = self.tokenize(text)    

            for text_token in text_tokens:
                if candidate not in final_result:
                    final_result[candidate] = 0
                final_result[candidate] += 1 if text_token in search_tokens else 0
        for key, score in final_result.items():
            heappush(heap,(score, key))
            if k and len(heap) > k:
                heappop(heap)

        transformed_heap = []
        for tpl in heap:
            transformed_heap.append((tpl[1], tpl[0]))
            
        return list(sorted(transformed_heap, reverse=True))