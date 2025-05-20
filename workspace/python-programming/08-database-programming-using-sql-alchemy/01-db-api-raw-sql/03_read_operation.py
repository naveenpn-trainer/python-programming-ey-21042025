from db_connection import get_sqlite_db_connection
db_connection = get_sqlite_db_connection()

cursor = db_connection.cursor()
cursor.execute("SELECT * from book_catalog")
books = cursor.fetchall()
for book in books:
    print(book)