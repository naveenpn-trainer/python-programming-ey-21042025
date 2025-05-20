import datetime

from db_connection import get_sqlite_db_connection
db_connection = get_sqlite_db_connection()

cursor = db_connection.cursor()
#  Not Recommended
# query = """
# INSERT INTO book_catalog (name, author, is_read, created_on) VALUES ('Python Programming', 'Abhilash', 0, '2025-05-16')
# """

query = """
INSERT INTO book_catalog (name, author, is_read, created_on) VALUES (?,?,?,?)
"""
cursor.execute(query, ("Java Programming","Naveen", False, datetime.date.today()))
db_connection.commit()
cursor.close()
db_connection.close()
