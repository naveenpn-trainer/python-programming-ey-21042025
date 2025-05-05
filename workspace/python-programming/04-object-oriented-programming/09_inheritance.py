class A:
    def __init__(self,message):
        print("A Constructor Invoked")
        self.message = message

    def print_message(self):
        print(f"Message= {self.message}")

class B(A):

    def print_message(self):
        print(f"Message= {self.message}")


if __name__ == '__main__':
    b = B()