from io import StringIO
import Configparcer
import JSON_ser
import Pickle_ser
import YAML_ser


def test_configparcer():
    """
    Add a new entry in the phone book
    >>> f1 = StringIO(Configparcer.set_config('JSON'))
    >>> f2 = StringIO(Configparcer.get_config())
    >>> f1.getvalue() == f2.getvalue()
    True
    """
    pass


def test_json():
    """
    Add a new entry in the phone book
    >>> f1 = StringIO(JSON_ser.save_phonebook("fhfgjgjg"))
    >>> f2 = StringIO(JSON_ser.init_phonebook())
    >>> f1.getvalue() == f2.getvalue()
    True
    """
    pass


def test_pickle():
    """
    Add a new entry in the phone book
    >>> f1 = StringIO(Pickle_ser.save_to_pickle("gdshgshs"))
    >>> f2 = StringIO(Pickle_ser.init_from_pickle())
    >>> f1.getvalue() == f2.getvalue()
    True
    """
    pass


def test_yaml():
    """
    Add a new entry in the phone book
    >>> f1 = StringIO(YAML_ser.save_to_yaml("dgdgdfghdf"))
    >>> f2 = StringIO(YAML_ser.load_from_yaml())
    >>> f1.getvalue() == f2.getvalue()
    True
    """
    pass
