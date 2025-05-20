import sqlite3

from mysql import connector


def get_sqlite_db_connection():
    db_connection = sqlite3.connect("book_catalog.db")
    return db_connection

def get_mysql_db_connection():
    db_connection = connector.connect(host="localhost",
                                      user="root",
                                      password="qwerty",
                                      database="book_catalog")
    return db_connection