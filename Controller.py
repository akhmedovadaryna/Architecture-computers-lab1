__author__ = 'alexandr'

import Business_logic as bl

#вывод приветствия
print("PHONEBOOK v1.0.2")

bl.get_phonebook()


while(1):
    print(" MENU ")
    print("Press 1 if you want see phonebook")
    print("Press 2 if you want add new record to phonebook")
    print("Press 3 if you want delete something from phonebook")
    print("Press 4 if you want edit something in phonebook")
    print("Press 5 if you want find something in phonebook")
    print("Press 0 if you want exit")
    choise = int(input("Enter your choise :  "))

    if choise == 0:
        break
    elif choise == 1:
        #вывод фонебука
        pass
    elif choise == 2:
        #ввод новой записи
        bl.add(new_number, new_FIO, new_street, new_house)
        #вывод добавленной строки
    elif choise == 3:
        #выбор что удалять
        bl.delete(phone_number)
    elif choise == 4:
        #выбор строчки для редактирования
        #ввод новых значений
        bl.change(key, number, FIO, street, house)
    elif choise == 5:
        #ввод критериев поиска
        bl.find(something)
    else:
        #некорректный выбор
        pass

print("Thank you!")


