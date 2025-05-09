class Book:
    def __init__(self, name, author,created_on):
        self._name = name
        self._author = author
        self._is_read=False
        self._create_on = created_on

    @property
    def name(self):
        return self._name

    @name.setter
    def is_read(self, value):
        self._is_read = value

    def __str__(self):
        return f"Name={self.name} Author={self._author}, Is Read={self._is_read}, Created on: {self._create_on}"

class BookOperations:
    BOOKS = []

    @staticmethod
    def add_book(name,author,created_on):
        book = Book(name, author, created_on)
        BookOperations.BOOKS.append(book)

    @staticmethod
    def list_books():
        for book in BookOperations.BOOKS:
            print(book)

    @staticmethod
    def mark_book_as_read(name):
        for book in BookOperations.BOOKS:
            if book.name == name:
                book.is_read = True


    @staticmethod
    def delete_book(name):
        for book in BookOperations.BOOKS:
            if book.name == name:
                BookOperations.BOOKS.remove(book)