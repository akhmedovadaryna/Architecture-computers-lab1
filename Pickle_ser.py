import pickle
__author__ = 'vadym'


list_with_dict = []


def save_to_pickle():
    with open('phonebook.pickle', 'wb') as file:
        pickle.dump(list_with_dict, file)


def init_from_pickle():
    with open('phonebook.pickle', 'rb') as file:
        pickle.load(file)
