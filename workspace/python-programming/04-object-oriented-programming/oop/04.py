class A:
    def m1(self):
        print("A m1()")

class B(A):
    def m1(self):
        print("B m1()")


class C(A):
    def m1(self):
        print("C m1()")

class AlphUtility:
    @staticmethod
    def invoke_method(obj:A):
        obj.m1()

if __name__ == '__main__':
    b = B()
    # b.m1()
    c = C()
    # c.m1()
    # AlphUtility.invoke_method(b)
    # AlphUtility.invoke_method(c)
