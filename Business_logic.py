import json
file_name = "phonebook"


list_with_dict = []


def save_phonebook():
    with open(file_name, 'w') as file:
        json.dump(list_with_dict, file)


def init_phonebook():
    file = open(file_name, 'r')
    global list_with_dict
    list_with_dict = json.load(file)
    file.close()


def add(number, FIO, street, house):
    """
    Add a new entry in the phone book
    >>> add(1111,'III', 'QQQ', 55)
    1111
    """
    list_with_dict.append({'number': number, 'FIO': FIO,
                           'street': street, 'house': house})
    save_phonebook()
    i = len(list_with_dict)-1
    dct = list_with_dict[i]
    return dct.get('number')


def delete(value):
    """
    Delete an entry from the phone book
    >>> delete(1234)
    0
    """
    i = 0
    flag = 0
    for dct in list_with_dict:
        if dct.get('number') != value:
            i = i+1
        else:
            flag = 1
            list_with_dict.pop(i)
    save_phonebook()
    return flag


def change(key, number='', FIO='', street='', house=''):
    """
    Change the entry in the phone book
    >>> change(4567,435,'III')
    0
    """
    flag = 0
    l = [number, FIO, street, house]
    list = ['number', 'FIO', 'street', 'house']
    for dct in list_with_dict:
        if dct.get('number') == key:
            flag = 1
            j = 0
            while j <= 3:
                if l[j] == '':
                    j = j+1
                    continue
                else:
                    dct[list[j]] = l[j]
                    j = j+1
    save_phonebook()
    return flag


def find(number='', FIO='', street='', house=''):
    """
    Find an entry in the phone book
    """
    i = 0
    q = []
    l = ['number', 'FIO', 'street', 'house']
    list = [number, FIO, street, house]
    for dct in list_with_dict:
        j = 0
        a = 0
        b = 0
        while j <= 3:
            if list[j] == '':
                b = b + 1
            elif dct.get(l[j]) == list[j]:
                a = a + 1
            j = j + 1

        if a == 4 - b:
            q.append(dct)
    return q
