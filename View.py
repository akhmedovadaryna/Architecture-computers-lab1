__author__ = 'vadym'


def view_phonebook(list_with_dict):  # вывод фонбука
    for i in list_with_dict:
        print(i)


def read_new_contact():  # ввод новой записи
    print("Telephone number: ")
    new_number = input()
    print("FIO: ")
    new_fio = input()
    print("Street: ")
    new_street = input()
    print("House: ")
    new_house = input()
    return new_number, new_fio, new_street, new_house


def del_choice():  # выбор что удалять
    print("Choose what number do you want to delete: ")
    phone_number = input()
    return phone_number


def edit_choice():  # выбор строчки для редактирования
    print("Print what number do you want to edit: ")
    key = input()
    return key


def new_values():  # ввод новых значений
    print("Enter new number: ")
    number = input()
    print("Enter new FIO: ")
    fio = input()
    print("Enter new street: ")
    street = input()
    print("Enter new house: ")
    house = input()
    return number, fio, street, house


def what_to_find():  # ввод критериев поиска
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


def uncorrect():  # некорректный ввод
    print("You have entered invalid values!")
