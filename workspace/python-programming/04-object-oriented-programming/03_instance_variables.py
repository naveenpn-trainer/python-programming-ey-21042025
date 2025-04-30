class A:
    y = 0
    def __init__(self,x):
        self.x = x
        A.y+=1

    def set_x(self,x):
        self.x = x

    def get_x(self):
        return self.x

    def print_values(self):
        print(f"{self.x}-{A.y}")

    @staticmethod
    def get_y():
        return A.y

if __name__ == '__main__':
    obj1 = A(10)
    obj2 = A(20)
    obj3 = A(20)
    print(obj1.get_x())
    obj1.set_x(100)
    print(obj2.get_x())
    print(obj1.get_x())
    obj1.print_values()
    print(A.get_y())