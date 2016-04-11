import unittest
from mock import Mock
from mock import patch
import BusinessLogic
import Config

__author__ = 'vadym'

pb = BusinessLogic.Phonebook({"number": "380991966445", "house": "14", "street": "Slobidska", "FIO": "Serov"})


class Tests(unittest.TestCase):
    def test_init(self):
        with patch('BusinessLogic.Phonebook.__init__') as perm_mock:
            perm_mock({"number": "380991966445", "house": "14", "street": "Slobidska", "FIO": "Serov"})
            perm_mock.assert_called_once_with(
                    {"number": "380991966445", "house": "14", "street": "Slobidska", "FIO": "Serov"})

        #    @mock.patch('BusinessLogic.Phonebook.__iter__')
        #    def test_iter(self, b):
        #        b.index = -1
        #        self.assertEqual('BusinessLogic.Phonebook.__iter__.index', -1)

        #    @mock.patch('BusinessLogic.Phonebook.find')
        #    def test_find(self, a):
        #        a.q = []
        #        self.assertEqual('BusinessLogic.Phonebook.find', a)

    def test_add(self):
        with patch('BusinessLogic.Phonebook.add') as perm_mock:
            perm_mock({'number': '123', 'FIO': 'fio',
                       'street': 'street', 'house': 'house'})
            perm_mock.assert_called_once_with({'number': '123', 'FIO': 'fio',
                                               'street': 'street', 'house': 'house'})

    def test_delete(self):
        with patch('BusinessLogic.Phonebook.delete') as perm_mock:
            perm_mock()
            perm_mock.assert_called()

    def test_change(self):
        with patch('BusinessLogic.Phonebook.change'):
            perm_mock = Mock(return_value=None)
            perm_mock('key')
            perm_mock('number')
            perm_mock('fio')
            perm_mock('street')
            perm_mock('house')
            perm_mock.assert_any_call('key')

    def test_find(self):
        with patch('BusinessLogic.Phonebook.find') as perm_mock:
            perm_mock(['number', 'FIO', 'street', 'house'])
            perm_mock.assert_called_once_with(['number', 'FIO', 'street', 'house'])

    def test_set_method_serialization(self):
        with patch('Config.Config.set_method_serialization') as perm_mock:
            perm_mock('method')
            perm_mock.assert_called_once_with('method')

    def test_set_controller(self):
        with patch('Config.Config.set_controller') as perm_mock:
            perm_mock('controller')
            perm_mock.assert_called_once_with('controller')

    def test_controller_init(self):
        with patch('Controller2.Controller.__init__'):
            perm_mock = Mock(return_value=None)
            perm_mock('config')
            perm_mock('serialization')
            perm_mock('phonebook')
            perm_mock.assert_any_call('config')

    def test_controller_start(self):
        with patch('Controller2.Controller.start'):
            perm_mock = Mock(return_value=None)
            perm_mock('0')
            perm_mock('1')
            perm_mock('2')
            perm_mock.assert_any_call('1')

if __name__ == '__main__':
    unittest.main()
