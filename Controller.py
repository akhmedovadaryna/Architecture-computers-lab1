import Business_logic
import View
import Pickle_ser
import JSON_ser
import YAML_ser
import Configparcer

list_with_dict = []


def menu():
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
    View.view_phonebook(list_with_dict)
    press_any_key()


def add():
    """
    Add new record
    :return: None
    """
    # ввод новой записи
    new_number, new_fio, new_street, new_house = View.read_new_contact()
    Business_logic.add(list_with_dict, new_number, new_fio, new_street, new_house)

    print("Successfull!")
    press_any_key()


def delete():
    """
    Delete record
    :return: None
    """
    # выбор что удалять
    if Business_logic.delete(list_with_dict, View.del_choice()):
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

    if Business_logic.change(list_with_dict, key, number, fio, street, house):
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
    View.view_phonebook(Business_logic.find(list_with_dict, number, fio, street, house))
    press_any_key()


def edit_conf_menu():
    print("Press 1 Set JSON")
    print("Press 2 Set PICKLE")
    print("Press 3 Set YAML")
    print("Press 0 if you want exit")
    return input("Enter your choise :  ")


def edit_conf(choise):
    if choise is '1':
        Configparcer.set_config("JSON")
    elif choise is '2':
        Configparcer.set_config("PICKLE")
    elif choise is '3':
        Configparcer.set_config("YAML")
    elif choise is not '0':
        print("Wrong! Enter again.\n")
        edit_conf_menu()


def save():
    conf = Configparcer.get_cofig()
    if conf == "JSON":
        JSON_ser.save_phonebook(list_with_dict)
    elif conf == "PICKLE":
        Pickle_ser.save_to_pickle(list_with_dict)
    elif conf == "YAML":
        YAML_ser.save_to_yaml(list_with_dict)


def load():
    global list_with_dict
    conf = Configparcer.get_cofig()
    if conf == "JSON":
        list_with_dict = JSON_ser.init_phonebook()
    elif conf == "PICKLE":
        list_with_dict = Pickle_ser.init_from_pickle()
    elif conf == "YAML":
        list_with_dict = YAML_ser.load_from_yaml()



# вывод приветствия
print("PHONEBOOK v1.0.3")


while 1:

    choise = menu()
    if choise == '0':
        break
    elif choise == '1':
        load()
    elif choise == '2':
        save()
    elif choise == '3':
        # вывод телефонной книги
        view()

    elif choise == '4':
        # добавление новой записи
        add()

    elif choise == '5':
        # удаление записи
        delete()

    elif choise == '6':
        # изменение записи
        edit()

    elif choise == '7':
        # поиск по телефонной книге
        find()

    elif choise == '8':
        edit_conf(edit_conf_menu())

    elif choise == '9':
        print(Configparcer.get_cofig())
        press_any_key()

    else:
        # некорректный выбор
        View.uncorrect()

print("Thank you!")
