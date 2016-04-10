import json

__author__ = 'alexandr'


# https://github.com/akhmedovadaryna/Phonebook/blob/master/phonebook

class Phonebook:
    def __init__(self):
        with open("phonebook", 'r') as file:
            self.phone_list = json.load(file)

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index == len(self.phone_list) - 1:
            raise StopIteration
        self.index += 1
        return self.phone_list[self.index]

    def add(self, number, fio, street, house):
        self.phone_list.append({'number': number, 'FIO': fio,
                                'street': street, 'house': house})

    def delete(self, value):
        i = 0
        for dct in self.phone_list:
            if dct.get('number') != value:
                i += 1
            else:
                self.phone_list.pop(i)

    def change(self, key, number='', fio='', street='', house=''):
        l = [number, fio, street, house]
        l_list = ['number', 'FIO', 'street', 'house']
        for dct in self.phone_list:
            if dct.get('number') == key:
                j = 0
                while j <= 3:
                    if l[j] == '':
                        j += 1
                        continue
                    else:
                        dct[l_list[j]] = l[j]
                        j += 1

    def find(self, number='', fio='', street='', house=''):
        q = []
        l = ['number', 'FIO', 'street', 'house']
        l_list = [number, fio, street, house]
        for dct in self.phone_list:
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


obj = Phonebook()

for i in obj:
    print(i)
