__author__ = 'alexandr'


class Config:
    def __init__(self):
        self.__method = ''
        self.__controller = 0
        self.__load_config()

    def set_method_serialization(self, method):
        self.__method = method
        self.__save_config()

    def set_controller(self, controller):
        self.__controller = controller
        self.__save_config()

    def get_method_serialization(self):
        return self.__method

    def get_controller(self):
        return self.__controller

    def __save_config(self):
        with open("config", 'wt') as file:
            #    file.write("method serialization = " + self.method)
            file.write(self.__method)
            file.write('\n')
            file.write(str(self.__controller))
            #   file.write("type controller = " + str(self.controller))

    def __load_config(self):
        with open("config", 'rt') as file:
            self.__controller = file.readline()
            self.__method = file.readline()

    def view(self):
        print(self.__controller)
        print(self.__method)



