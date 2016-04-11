from BusinessLogic import Phonebook
from View2 import View

__author__ = 'alexandr'


class Controller:
    def __init__(self, phonebook, serialization, config):
        self.config = config
        self.serialization = serialization
        self.phonebook = phonebook

    def __menu(self):
        """
        print MENU and ask user's choise
        :return: user's choise
        """

        print("\n MENU ")
        print("Press 1 if you want load phonebook")
        print("Press 2 if you want save phonebook")
        print("Press 3 if you want see phonebook")
        print("Press 4 if you want add new record to phonebook")
        print("Press 5 if you want delete something from phonebook")
        print("Press 6 if you want edit something in phonebook")
        print("Press 7 if you want find something in phonebook")
        print("Press 8 if you want edit config")
        print("Press 9 if you want view config")
        print("Press 0 if you want exit")
        return input("Enter your choise :  ")

    def __press_any_key(self):
        """
        Wait for user
        :return: None
        """
        input("Press Enter to continue...")

    def view(self):
        """
        Print Phonebook
        :return: None
        """
        self.phonebook.view_phonebook()
        self.__press_any_key()

    def add(self):
        """
        Add new record
        :return: None
        """

        new_number, new_fio, new_street, new_house = View.read_new_contact()
        self.phonebook.add(new_number, new_fio, new_street, new_house)

        print("Successfull!")
        self.__press_any_key()

    def delete(self):
        """
        Delete record
        :return: None
        """
        if self.phonebook.delete(View.del_choice()):
            print("Successfull!")
        else:
            print("Not found!")
        self.__press_any_key()

    def edit(self):
        """
        Edit record
        :return: None
        """
        key = View.edit_choice()
        number, fio, street, house = View.new_values()

        if self.phonebook.change(key, number, fio, street, house):
            print("Successfull!")
        else:
            print("Not found!")
        self.__press_any_key()

    def find(self):
        """
        Search in Phonebook
        :return: None
        """
        number, fio, street, house = View.what_to_find()
        self.phonebook.view_phonebook(self.phonebook.find(number, fio, street, house))
        self.__press_any_key()

    def edit_conf_menu(self):
        print("Press 1 Set JSON")
        print("Press 2 Set PICKLE")
        print("Press 3 Set YAML")
        print("Press 0 if you want exit")
        return input("Enter your choise :  ")

    def edit_conf(self, ch):
        if ch is '1':
            self.config.set_method_serialization("JSON")
        elif ch is '2':
            self.config.set_method_serialization("PICKLE")
        elif ch is '3':
            self.config.set_method_serialization("YAML")
        elif ch is not '0':
            print("Wrong! Enter again.\n")
            self.edit_conf_menu()

    def save(self):
        conf = self.config.get_method_serialization()
        if conf == "JSON":
            self.serialization.save_phonebook_in_json(self.phonebook.get_phone_list())
        elif conf == "PICKLE":
            self.serialization.save_to_pickle(self.phonebook.get_phone_list())
        elif conf == "YAML":
            self.serialization.save_to_yaml(self.phonebook.get_phone_list())

    def load(self):
        conf = self.config.get_method_serialization()
        if conf == "JSON":
            self.phonebook.set_phone_list(self.serialization.load_phonebook_from_json())
        elif conf == "PICKLE":
            self.phonebook.set_phone_list(self.serialization.load_from_pickle())
        elif conf == "YAML":
            self.phonebook.set_phone_list(self.serialization.load_from_yaml())

    def start(self):
        print("PHONEBOOK v2.0.4")

        while 1:

            choise = self.__menu()
            if choise == '0':
                break
            elif choise == '1':
                self.load()
            elif choise == '2':
                self.save()
            elif choise == '3':
                self.view()

            elif choise == '4':
                self.add()

            elif choise == '5':
                self.delete()

            elif choise == '6':
                self.edit()

            elif choise == '7':
                self.find()

            elif choise == '8':
                self.edit_conf(self.edit_conf_menu())

            elif choise == '9':
                print(self.config.get_controller())
                print(self.config.get_method_serialization())
                self.__press_any_key()

            else:
                View.uncorrect()

        print("Thank you!")
