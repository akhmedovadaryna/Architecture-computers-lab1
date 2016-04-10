import json

file_name = "phonebook"


def save_phonebook(list_with_dict):
    """
    Open file_name and save phonebook
    :param list_with_dict:
    :return:
    """
    with open(file_name, 'w') as file:
        json.dump(list_with_dict, file)
    return list_with_dict


def init_phonebook():
    """
    Open file_name and init phonebook
    :return:
    """
    with open(file_name, 'r') as file:
        list_with_dict = json.load(file)
    return list_with_dict
