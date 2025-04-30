class A:
    def __init__(self,x):
        self.x = x

    def get_x(self):
        return self.x

    def set_x(self,x):
        self.x = x

if __name__ == '__main__':
    obj1 = A(100)
    obj2 = obj1
    obj1.set_x(10)
    print(obj1.get_x())
    print(obj2.get_x())