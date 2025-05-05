class User:

    def __init__(self, id, name):
        self.id = id
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

if __name__ == '__main__':
    u = User(1,"naveen pn")
    print(u.name)
    u.name = "Naveen Pn"
    print(u.name)