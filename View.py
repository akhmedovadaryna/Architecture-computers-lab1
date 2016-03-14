__author__ = 'vadym'

file_name = "phonebook"


def view_phonebook(phonebook):  # вывод фонбука
    print(phonebook)

def read_new_contact():  # ввод новой записи
    print("Telephone number: ")
    new_number = input()
    print("FIO: ")
    new_FIO = input()
    print("Street: ")
    new_street = input()
    print("House: ")
    new_house = input()


def view_new_contact(contact):  # вывод добавленной строки
    print(contact)


def del_choice():  # выбор что удалять
    print("Choose what number do you want to delete: ")
    phone_number = input()


def edit_choice():  # выбор строчки для редактирования
    print("Print what number do you want to edit: ")
    key = input()


def new_values(): # ввод новых значений
    print("Enter new number: ")
    number = input()
    print("Enter new FIO: ")
    FIO = input()
    print("Enter new street: ")
    street = input()
    print("Enter new house: ")
    house = input()


def what_to_find(): #ввод критериев поиска
    print("Enter what do you want to find: ")
    something = input()

def uncorrect(): # некорректный ввод
    print("You have entered invalid values!")