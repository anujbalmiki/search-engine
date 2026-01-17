import re

def tokenize(text):
    if not isinstance(text, str):
        raise ValueError("Document must be a non-empty string")
    tokens = []
    cleaned = re.sub(r'[^\w\s]', '', text.lower())
    tokens = [t for t in cleaned.split() if t]

    return tokens