'''

1. If we create an object of Derived class it is mandatory to call the base class constructor
'''

class A:
    def __init__(self):
        print("A Constructor Invoked")


class B(A):
    pass


if __name__ == '__main__':
    b = B()