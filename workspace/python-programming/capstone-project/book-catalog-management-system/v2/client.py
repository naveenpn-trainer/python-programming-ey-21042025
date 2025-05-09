from datetime import datetime
import sys
from book_operations import BookOperations
import menu

if __name__ == '__main__':
    BookOperations.load_books()
    BOOKS = []
    while True:
        print(menu.MENU)
        user_input = input("Enter your choice")
        match user_input:
            case "1":
                name = input("Enter book name")
                author = input("Enter author name")
                created_on = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                book = {'Name':name,'Author':author,'IsRead':False,'created_on':created_on}
                BookOperations.add_book(name,author,created_on)
            case "2":
                BookOperations.list_books()
            case "3":
                name = input("Enter book name")
                BookOperations.mark_book_as_read(name)
            case "4":
                name = input("Enter book name")
                BookOperations.delete_book(name)
            case "q":
                print("Application terminates...")
                sys.exit(1)
            case _:
                print("Invalid Input")