

file_name = "config"
def set_config(conf):
    with open(file_name, 'wt') as file:
        file.write(conf)


def get_cofig():
    with open(file_name, 'rt') as file:
        conf = file.read()
    return conf