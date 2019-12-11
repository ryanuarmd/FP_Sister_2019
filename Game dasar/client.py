import Pyro4


def get_fileserver_object(instance_name):
    uri = "PYRONAME:{}@localhost:7777" . format(instance_name)
    fserver = Pyro4.Proxy(uri)
    return fserver


if __name__ == '__main__':
    connection = get_fileserver_object("hostname")
    print(connection.hello())
