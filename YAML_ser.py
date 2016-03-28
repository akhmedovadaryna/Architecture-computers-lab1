import yaml


def save_to_yaml(list_with_dict):
    with open("phonebook.YAML", "w") as file:
        yaml.dump(list_with_dict, file)
    return list_with_dict


def load_from_yaml():
    with open("phonebook.YAML", "r") as file:
        list_with_dict = yaml.load(file)
    return list_with_dict
