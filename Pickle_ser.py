import pickle


def save_to_pickle(list_with_dict):
    """
    Open file and save in pickle
    :param list_with_dict:
    :return:
    """
    with open('phonebook.pickle', 'wb') as file:
        pickle.dump(list_with_dict, file)
    return list_with_dict


def init_from_pickle():
    """
    Open file and load from pickle
    :return:
    """
    with open('phonebook.pickle', 'rb') as file:
        list_with_dict = pickle.load(file)
    return list_with_dict
