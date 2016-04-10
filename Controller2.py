__author__ = 'alexandr'


class Controller:
    def __init__(self, phonebook, serialization, config):
        self.config = config
        self.serialization = serialization
        self.phonebook = phonebook

    def action(self):
        print("bla bla")
        self.__action2()

    def __action2(self):
        print("haha")



obj = Controller(1, 2, 3)
obj.action()
