__author__ = 'alexandr'


class View:
    """
    class View
    """
    @staticmethod
    def read_new_contact():
        """
        Input new contact
        :return:
        """
        print("Telephone number: ")
        new_number = input()
        print("FIO: ")
        new_fio = input()
        print("Street: ")
        new_street = input()
        print("House: ")
        new_house = input()
        return new_number, new_fio, new_street, new_house

    @staticmethod
    def del_choice():
        """
        Input number for delete
        :return:
        """
        print("Choose what number do you want to delete: ")
        phone_number = input()
        return phone_number

    @staticmethod
    def edit_choice():
        """
        Input number for edit
        :return:
        """
        print("Print what number do you want to edit: ")

        key = input()
        return key

    @staticmethod
    def new_values():
        """
        Input new value
        :return:
        """
        print("Enter new number: ")
        number = input()
        print("Enter new FIO: ")
        fio = input()
        print("Enter new street: ")
        street = input()
        print("Enter new house: ")
        house = input()
        return number, fio, street, house

    @staticmethod
    def what_to_find():
        """
        Input for find
        :return:
        """
        print("Enter the search criteria" +
              "(if it's not necessary you don't need to write it): ")
        print("Enter searching number: ")
        number = input()
        print("Enter searching FIO: ")
        fio = input()
        print("Enter searching street: ")
        street = input()
        print("Enter searching house: ")
        house = input()
        return number, fio, street, house

    @staticmethod
    def uncorrect():
        print("You have entered invalid values!")
