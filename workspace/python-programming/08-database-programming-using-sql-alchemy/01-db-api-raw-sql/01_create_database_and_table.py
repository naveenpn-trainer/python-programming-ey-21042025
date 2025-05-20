import sqlite3
from mysql import connector

def initialize_with_sqlite():
    db_connection = sqlite3.connect("book_catalog.db")
    query = """
    CREATE TABLE book_catalog (
    	id INTEGER NOT NULL PRIMARY KEY, 
    	name VARCHAR(100), 
    	author VARCHAR(100), 
    	is_read BOOLEAN, 
    	created_on DATE
    )
    """
    cursor = db_connection.cursor()
    cursor.execute(query)
    cursor.close()
    db_connection.close()

def initialize_with_mysql():
    db_connection = connector.connect(host="localhost",
                                      user="root",
                                      password="qwerty",
                                      database="book_catalog")

    cursor = db_connection.cursor()

    query = """
    CREATE TABLE book_catalog (
        id INTEGER NOT NULL, 
        name VARCHAR, 
        author VARCHAR, 
        is_read BOOLEAN, 
        created_on DATE, 
        PRIMARY KEY (id)
    )
    """
    cursor.execute(query)
    cursor.close()
    db_connection.close()

if __name__ == '__main__':
    initialize_with_sqlite()