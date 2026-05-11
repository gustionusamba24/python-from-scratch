def merge(dict1: dict, dict2: dict) -> dict:
    merged_dicts = {}

    for key, value in dict1.items():
        merged_dicts[key] = value

    for key, value in dict2.items():
        merged_dicts[key] = value 

    return merged_dicts