class Person:
    def __init__(self):
        self.name = 10
        self._status = 1
        self.__secret = 100

    def modify_z(self):
        self.__secret = 100

    def get_z(self):
        return self.__secret


if __name__ == '__main__':
    obj1 = Person()
    print(obj1.name)
    print(obj1._status)
    # print(obj1.__z)
    print(obj1._Person__secret) ## Mangling