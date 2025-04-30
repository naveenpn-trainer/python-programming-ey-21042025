class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages
        print("Constructor Invoked")

    def __str__(self):
        return f"Title={self.title}, Pages={self.pages}"

    def __len__(self):
        return self.pages

    def __add__(self, other):
        return Book(f"{self.title} & {other.title}", {self.pages+other.pages})

if __name__ == '__main__':
    book1 = Book("Python Programming Volume 01",100)
    book2 = Book("Python Programming Volume 02", 150)
    print(book1)
    print(len(book1))
    book3 = book1 + book2
    print(book3)

    L1 = [1,2,3]
    L2 = [4,5,6]
    print(L1+L2)
