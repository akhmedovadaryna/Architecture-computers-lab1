def add(list_with_dict, number, fio, street, house):
    """
    Add a new entry in the phone book
    >>> add(1111, 'III', 'QQQ', 55)
    1111
    """
    list_with_dict.append({'number': number, 'FIO': fio,
                           'street': street, 'house': house})
    i = len(list_with_dict) - 1
    dct = list_with_dict[i]
    return dct.get('number')


def delete(list_with_dict, value):
    """
    Delete an entry from the phone book
    >>> delete(1234)
    0
    """
    i = 0
    flag = 0
    for dct in list_with_dict:
        if dct.get('number') != value:
            i += 1
        else:
            flag = 1

            list_with_dict.pop(i)
    return flag


def change(list_with_dict, key, number='', fio='', street='', house=''):
    """
    Change the entry in the phone book
    >>> change(4567, 435, 'III')
    0
    """
    flag = 0
    l = [number, fio, street, house]
    l_list = ['number', 'FIO', 'street', 'house']
    for dct in list_with_dict:
        if dct.get('number') == key:
            flag = 1
            j = 0
            while j <= 3:
                if l[j] == '':
                    j += 1
                    continue
                else:
                    dct[l_list[j]] = l[j]
                    j += 1
    return flag


def find(list_with_dict, number='', fio='', street='', house=''):
    """
    Find an entry in the phone book
    """
    q = []
    l = ['number', 'FIO', 'street', 'house']
    l_list = [number, fio, street, house]
    for dct in list_with_dict:
        j = 0
        a = 0
        b = 0
        while j <= 3:
            if l_list[j] == '':
                b += 1
            elif dct.get(l[j]) == l_list[j]:
                a += 1
            j += 1

        if a == 4 - b:
            q.append(dct)
    return q
