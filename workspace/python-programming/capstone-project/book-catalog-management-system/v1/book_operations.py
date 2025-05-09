from datetime import datetime
import sys

MENU = '''
1. Add a book
2. List all books
3. Mark a given book as read
4. Delete a book by name
q. To Quit
'''

if __name__ == '__main__':
    BOOKS = []
    while True:
        print(MENU)
        user_input = input("Enter your choice")
        if user_input=='1':
            name = input("Enter book name")
            author = input("Enter author name")
            created_on = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            book = {'Name':name,'Author':author,'IsRead':False,'created_on':created_on}
            BOOKS.append(book)
        elif user_input == "2":
            for book in BOOKS:
                print(book)
        elif user_input =="3":
            name = input("Enter book name")
            for book in BOOKS:
                if book['Name']==name:
                    book['IsRead'] = True
                    break
        elif user_input == "4":
            name = input("Enter book name")
            for book in BOOKS:
                if book['Name']==name:
                    BOOKS.remove(book)
                    break
        elif user_input == "q":
            print("Application terminates...")
            sys.exit(1)
        else:
            print("Invalid Input")