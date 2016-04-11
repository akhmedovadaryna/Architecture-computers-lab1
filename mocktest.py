import unittest

import mock
from mock import patch
import BusinessLogic as bl

pb = bl.Phonebook({"number": "380991966445", "house": "14", "street": "Slobidska", "FIO": "Serov"})


class tests(unittest.TestCase):
    def test_init(self):
        with patch('BusinessLogic.Phonebook.__init__') as perm_mock:
            perm_mock({"number": "380991966445", "house": "14", "street": "Slobidska", "FIO": "Serov"})
            perm_mock.assert_called_once_with({"number": "380991966445", "house": "14", "street": "Slobidska", "FIO": "Serov"})

    @mock.patch('BusinessLogic.Phonebook.__iter__')
    def test_iter(self, b):
        b.index = -1
        self.assertEqual(bl.Phonebook.__iter__, -1)

if __name__ == '__main__':
    unittest.main()
