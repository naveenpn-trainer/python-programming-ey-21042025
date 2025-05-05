class A:
    prop = "A value"

    @staticmethod
    def static_method():
        print(f"Static method: {A.prop}")


    @classmethod
    def class_method(cls):
        print(f"Class method: {cls.prop}")

class B(A):
    prop = "B value"

class C(A):
    prop = "C value"


if __name__ == '__main__':
    A.static_method()
    A.class_method()

    B.static_method()
    B.class_method()

    C.class_method()