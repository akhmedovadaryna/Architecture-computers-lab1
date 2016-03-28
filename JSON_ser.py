import json

file_name = "phonebook"


def save_phonebook(list_with_dict):
    with open(file_name, 'w') as file:
        json.dump(list_with_dict, file)
    return list_with_dict


def init_phonebook():
    with open(file_name, 'r') as file:
        list_with_dict = json.load(file)
    return list_with_dict
