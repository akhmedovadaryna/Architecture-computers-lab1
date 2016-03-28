import yaml

__author__ = 'vadym'

list_with_dict = []


def save_to_yaml():
    with open("phonebook.YAML", "wb") as file:
        yaml.dump(list_with_dict, file)


def load_from_yaml():
    with open("phonebook.YAML", "rb") as file:
        yaml.load(list_with_dict, file)