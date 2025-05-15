import json

BOOKS_FILE = "books.json"
from os.path import exists
class Book:
    def __init__(self, name, author, created_on):
        self._name = name
        self._author = author
        self._is_read= False
        self._create_on = created_on

    @property
    def is_read(self):
        return self._is_read

    @is_read.setter
    def is_read(self, value):
        self._is_read = value

    #      Convert Book object into dictionary (JSON Serialization)
    def to_dict(self):
        return {
            'name':self._name,
            'author':self._author,
            'is_read':self._is_read,
            'created_on':self._create_on
        }

    @staticmethod
    def from_dict(json_data):
        return Book(name=json_data['name'],
                    author=json_data['author'],
                    created_on=json_data['created_on'],
                    )
    def __str__(self):
        return f"Name={self._name} Author={self._author}, Is Read={self._is_read}, Created on: {self._create_on}"

class BookOperations:
    BOOKS = []

    @staticmethod
    def load_books():
        if exists(BOOKS_FILE):
            with open(BOOKS_FILE,'r') as file:
                data = json.load(file)
                print(data)
                BookOperations.BOOKS = [Book.from_dict(e) for e in data]

    @staticmethod
    def save_books():
        with open(BOOKS_FILE,'w') as file:
            json.dump([book.to_dict() for book in BookOperations.BOOKS], file, indent=4)


    @staticmethod
    def add_book(name, author, created_on):
        book = Book(name, author, created_on)
        BookOperations.BOOKS.append(book)
        BookOperations.save_books()
        print("Book added")

    @staticmethod
    def list_books():
        for book in BookOperations.BOOKS:
            print(book)

    @staticmethod
    def mark_book_as_read():
        pass