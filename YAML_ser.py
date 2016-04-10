import yaml


def save_to_yaml(list_with_dict):
    """
    Open file and save in yaml
    :param list_with_dict:
    :return:
    """
    with open("phonebook.YAML", "w") as file:
        yaml.dump(list_with_dict, file)
    return list_with_dict


def load_from_yaml():
    """
    Open file and load from yaml
    :return:
    """
    with open("phonebook.YAML", "r") as file:
        list_with_dict = yaml.load(file)
    return list_with_dict
