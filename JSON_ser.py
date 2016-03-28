import json

file_name = "phonebook"


def save_phonebook(list_with_dict):
    with open(file_name, 'wt') as file:
        json.dump(list_with_dict, file)


def init_phonebook():
    with open(file_name, 'rt') as file:
        list_with_dict = json.load(file)
    return list_with_dict
