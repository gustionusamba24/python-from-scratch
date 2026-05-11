dict_1 = {
    "a": 1, # because there is a different value
    "b": "hello",
    "c": True,
}

dict_2 = {
    "a": "1", # because there is a different value
    "b": "hello",
    "c": False,
}

print(dict_1 == dict_2)

dict_name_1 = {
    "name": "Alucard",
    "strength": 1500,
    "weapon": "Mighty Sword",
}

dict_name_2 = {
    "name": "Alucard",
    "strength": "1500",
    "weapon": "Blade of Kampilan",
}

different_value = {}

for key in dict_name_1:
    if dict_name_1[key] != dict_name_2[key]:
        different_value[key] = (dict_name_1[key], dict_name_2[key])

print(different_value)