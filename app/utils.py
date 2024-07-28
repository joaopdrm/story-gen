def validate_keywords(keywords:str):
    return all(isinstance(keyword, str) for keyword in keywords) and len(keywords) == 10