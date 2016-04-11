__author__ = 'alexandr'


class Config:
    def __init__(self):
        self.method = ''
        self.controller = 0
        self.load_config()

    def set_method_serialization(self, method):
        self.method = method
        self.save_config()

    def set_controller(self, controller):
        self.controller = controller
        self.save_config()

    def get_method_serialization(self):
        return self.method

    def get_controller(self):
        return self.controller

    def save_config(self):
        with open("config", 'wt') as file:
            #    file.write("method serialization = " + self.method)
            file.write(self.method)
            file.write('\n')
            file.write(str(self.controller))
            #   file.write("type controller = " + str(self.controller))

    def load_config(self):
        with open("config", 'rt') as file:
            self.controller = file.readline()
            self.method = file.readline()

    def view(self):
        print(self.controller)
        print(self.method)



