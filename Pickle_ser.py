import pickle


def save_to_pickle(list_with_dict):
    with open('phonebook.pickle', 'wb') as file:
        pickle.dump(list_with_dict, file)


def init_from_pickle():
    with open('phonebook.pickle', 'rb') as file:
        list_with_dict = pickle.load(file)
    return list_with_dict
