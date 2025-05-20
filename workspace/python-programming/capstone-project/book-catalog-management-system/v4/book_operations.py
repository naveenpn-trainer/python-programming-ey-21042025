import datetime
import sqlite3


class BookOperations:
    def __init__(self, db_path):
        self.db_path = db_path
        with sqlite3.connect(self.db_path) as db_connection:
            cursor = db_connection.cursor()
            query = """
            CREATE TABLE book_catalog (
            	id INTEGER NOT NULL PRIMARY KEY, 
            	name VARCHAR(100), 
            	author VARCHAR(100), 
            	is_read BOOLEAN, 
            	created_on DATE
            )
            """
            cursor.execute(query)
            db_connection.commit()

    def add_book(self, name, autor, create_on):
        print(self.db_path)
        with sqlite3.connect(self.db_path) as db_connection:
            cursor = db_connection.cursor()
            query = """
            INSERT INTO book_catalog (name, author, is_read, created_on) VALUES (?,?,?,?)
            """
            cursor.execute(query,(name, autor, False, create_on))

    def list_books(self):
        with sqlite3.connect(self.db_path) as db_connection:
            cursor = db_connection.cursor()
            query = """
            SELECT * from book_catalog
            """
            cursor.execute(query)
            books = cursor.fetchall()
            for book in books:
                print(book)
