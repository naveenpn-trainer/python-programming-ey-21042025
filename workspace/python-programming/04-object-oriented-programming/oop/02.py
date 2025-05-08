class A:
    def __init__(self, name):
        print("A Constructor Invoked")
        self.name = name

    def get_name(self):
        return self.name


class B(A):
    def __init__(self, name):
        A.__init__(self, name)
        # super().__init__(name)
        print("B Constructor Invoked")

    def get_name(self):
        return super().get_name()

if __name__ == '__main__':
    b = B("Naveen Pn")
    print(b.get_name())