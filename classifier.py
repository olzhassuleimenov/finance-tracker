import json

def open_json(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def transaction(dictionary, description):
    desc = str(description).lower()
    
    for category, keywords in dictionary.items():
        for key in keywords:
            if key in desc:
                return category
                
    return "Прочее" 