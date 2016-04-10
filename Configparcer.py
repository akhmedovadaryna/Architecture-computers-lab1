file_name = "config"


def set_config(conf):
    """
    Open file_name and save configuration
    :param conf:
    :return:
    """
    with open(file_name, 'wt') as file:
        file.write(conf)
    return conf


def get_config():
    """
    Open file_name and read configuration
    :return:
    """
    with open(file_name, 'rt') as file:
        conf = file.read()
    return conf
