file_name = "config"


def set_config(conf):
    with open(file_name, 'wt') as file:
        file.write(conf)
    return conf


def get_config():
    with open(file_name, 'rt') as file:
        conf = file.read()
    return conf
