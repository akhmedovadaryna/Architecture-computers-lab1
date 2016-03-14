import Business_logic
import View


def menu():
    """
    print MENU and ask user's choise
    :return: user's choise
    """

    print("\n MENU ")
    print("Press 1 if you want see phonebook")
    print("Press 2 if you want add new record to phonebook")
    print("Press 3 if you want delete something from phonebook")
    print("Press 4 if you want edit something in phonebook")
    print("Press 5 if you want find something in phonebook")
    print("Press 0 if you want exit")
    return input("Enter your choise :  ")


def press_any_key():
    """
    Wait for user
    :return: None
    """
    input("Press Enter to continue...")


def view():
    """
    Print Phonebook
    :return: None
    """
    View.view_phonebook(Business_logic.list_with_dict)
    press_any_key()


def add():
    """
    Add new record
    :return: None
    """
    # ввод новой записи
    new_number, new_fio, new_street, new_house = View.read_new_contact()
    Business_logic.add(new_number, new_fio, new_street, new_house)

    print("Successfull!")
    press_any_key()


def delete():
    """
    Delete record
    :return: None
    """
    # выбор что удалять
    if Business_logic.delete(View.del_choice()):
        print("Successfull!")
    else:
        print("Not found!")
    press_any_key()


def edit():
    """
    Edit record
    :return: None
    """
    # выбор строчки для редактирования
    key = View.edit_choice()
    # ввод новых значений
    number, fio, street, house = View.new_values()

    if Business_logic.change(key, number, fio, street, house):
        print("Successfull!")
    else:
        print("Not found!")
    press_any_key()


def find():
    """
    Search in Phonebook
    :return: None
    """
    # ввод критериев поиска
    number, fio, street, house = View.what_to_find()
    View.view_phonebook(Business_logic.find(number, fio, street, house))
    press_any_key()


# вывод приветствия
print("PHONEBOOK v1.0.3")
Business_logic.init_phonebook()

while 1:

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
        View.uncorrect()

print("Thank you!")
