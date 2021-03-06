import json
import pickle
import yaml

__author__ = 'alexandr'


class Serialization:
    """
    class Serialization
    """
    def __init__(self, file_name):
        self.__file_name = file_name

    def save_phonebook_in_json(self, obj):
        """
        save phone book in json
        """
        with open(self.__file_name, 'w') as file:
            json.dump(obj, file)

    def load_phonebook_from_json(self):
        """
        load phone book from json
        """
        with open(self.__file_name, 'r') as file:
            list_with_dict = json.load(file)
        return list_with_dict

    def save_to_pickle(self, obj):
        """
        save phone book in pickle
        """
        with open(self.__file_name + '.pickle', 'wb') as file:
            pickle.dump(obj, file)

    def load_from_pickle(self):
        """
        load phone book from pickle
        """
        with open(self.__file_name + '.pickle', 'rb') as file:
            list_with_dict = pickle.load(file)
        return list_with_dict

    def save_to_yaml(self, obj):
        """
        save phone book in yaml
        """
        with open(self.__file_name + ".YAML", "w") as file:
            yaml.dump(obj, file)

    def load_from_yaml(self):
        """
        load phone book from yaml
        """
        with open(self.__file_name + ".YAML", "r") as file:
            list_with_dict = yaml.load(file)
        return list_with_dict
