__author__ = 'alexandr'

import Business_logic as bl
import View as vw




def menu():
    '''
    print MENU and ask user's choise
    :return: user's choise
    '''

    print("\n MENU ")
    print("Press 1 if you want see phonebook")
    print("Press 2 if you want add new record to phonebook")
    print("Press 3 if you want delete something from phonebook")
    print("Press 4 if you want edit something in phonebook")
    print("Press 5 if you want find something in phonebook")
    print("Press 0 if you want exit")
    return input("Enter your choise :  ")

def press_any_key():
    '''
    Wait for user
    :return: None
    '''
    input("Press Enter to continue...")

def view():
    '''
    Print Phonebook
    :return: None
    '''
    vw.view_phonebook(bl.list_with_dict)
    press_any_key()

def add():
    '''
    Add new record
    :return: None
    '''
    # ввод новой записи
    new_number, new_FIO, new_street, new_house = vw.read_new_contact()
    bl.add(new_number, new_FIO, new_street, new_house)

    print("Successfull!")
    press_any_key()

def delete():
    '''
    Delete record
    :return: None
    '''
    # выбор что удалять
    if (bl.delete(vw.del_choice())):
        print("Successfull!")
    else:
        print("Not found!")
    press_any_key()

def edit():
    '''
    Edit record
    :return: None
    '''
    # выбор строчки для редактирования
    key = vw.edit_choice()
    # ввод новых значений
    number, FIO, street, house = vw.new_values()

    if (bl.change(key, number, FIO, street, house )):
        print("Successfull!")
    else:
        print("Not found!")
    press_any_key()

def find():
    '''
    Search in Phonebook
    :return: None
    '''
     # ввод критериев поиска
    number, FIO, street, house = vw.what_to_find()
    vw.view_phonebook(bl.find(number, FIO, street, house))
    press_any_key()


# вывод приветствия
print("PHONEBOOK v1.0.3")
bl.init_phonebook()

while(1):

    choise = menu()
    if choise == '0':
        break
    elif choise == '1':
        # вывод телефонной книги
        view()

    elif choise == '2':
        # добавление новой записи
        add()

    elif choise == '3':
        # удаление записи
        delete()

    elif choise == '4':
        # изменение записи
        edit()

    elif choise == '5':
        # поиск по телефонной книге
        find()
    else:
        # некорректный выбор
        vw.uncorrect()

print("Thank you!")


