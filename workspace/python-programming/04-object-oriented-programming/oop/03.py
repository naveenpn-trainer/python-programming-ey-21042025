class A:
    # def m1(self, id):
    #     print(f"m1 (int): {id}")
    #
    # def m1(self, name):
    #     print(f"m1 (string): {name}")

    def m1(self, id = None, name=None):
        print(f"Name= {name} Id={id}")

if __name__ == '__main__':
    obj = A()
    obj.m1(id=10, name="Naveen Pn")