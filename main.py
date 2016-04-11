from BusinessLogic import Phonebook
from Config import Config
from Controller2 import Controller
from Serialization import Serialization
import Controller as Control

__author__ = 'alexandr'

if __name__ == "__main__":
    conf = Config()
    if conf.get_controller() == '1\n':
        obj = Controller(Phonebook([]), Serialization("phonebook"), conf)
        obj.start()
    elif conf.get_controller() == '0\n':
        Control.main()
