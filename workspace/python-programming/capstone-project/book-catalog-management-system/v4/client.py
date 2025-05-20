from book_operations import BookOperations
from menu import MENU
from datetime import datetime
if __name__ == '__main__':
    book_operations = BookOperations("book_catalog.db")
    while True:
        print(MENU)
        user_input = input("Enter your choice")
        match user_input:
            case "1":
                name = input("Enter book name")
                author = input("Enter author name")
                create_on = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                book_operations.add_book(name,author, create_on)
            case "2":
                book_operations.list_books()


