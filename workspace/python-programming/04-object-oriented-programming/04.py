class A:
    x = 10

    @staticmethod
    def static_method():
        print(A.x)

    @classmethod
    def class_method(cls):
        print(cls.x)


if __name__ == '__main__':
    A.static_method()
    A.class_method()