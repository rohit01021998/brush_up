'''
Library Management System

Design classes for Book, Member, and Library.

Implement borrowing, returning, and checking availability.
Use inheritance if there are different types of books (e.g., ReferenceBook, Ebook).

Use dictionary lists tuples and sets where ever possible.
'''

import datetime
import random

given_book_record = {}
taken_book_record = {}
book_ids = []
book_count = 0

class Book():
    def __init__(self, book_id, book_name, book_author):
        self.book_id = book_id
        self.book_name = book_name
        self.book_author = book_author
        self.taken_on = datetime.datetime.now()
        self.submitted_status = 'Pending'
    
    def submitted_on(self):
        self.submitted_status = datetime.datetime.now()
        return f"Submitted on {self.submitted_status}"

def main():
    global book_count

    print("\nPlease enter your choice: ")
    print("1. To give book")
    print("2. To receive book")
    print("3. Check details of book given")
    print("4. Check details of book taken")
    print("5. Check detail of book from book ID")
    
    user_input  = int(input("\nType your number: "))
    if type(user_input)!=int:
        print("input not an integer")
    else:
        if user_input==1:
            book_name = input("Enter Book Name: ")
            author_name = input("Enter Author Name: ")
            book_id = random.randint(1000,9999)
            print(f'\nNew Book ID generated {book_id}')
            while book_id in book_ids: book_id = random.randint(1000,9999)
            book_ids.append(book_id)
            new_book = Book(book_id, book_name, author_name)
            given_book_record[book_id]=new_book
            book_count += 1
        elif user_input==2:
            search_input=int(input("\nEnter the book id: "))
            book_object_details = given_book_record[search_input]
            print(f"\nBook name: {book_object_details.book_name}")
            print(f"Book author:{book_object_details.book_author}")
            book_count -= 1
            taken_book_record[search_input]=given_book_record[search_input]
            taken_book_record[search_input].submitted_on()
            del given_book_record[search_input]

        elif user_input==3:
            print(given_book_record)

        elif user_input==4:
            print(taken_book_record)
        
        elif user_input==5:
            search_input=int(input("\nEnter the book id: "))
            book_object_details = given_book_record[search_input] if search_input in given_book_record else taken_book_record[search_input]
            print('\nBook has been given') if search_input in given_book_record else print('book has been taken')
            print(f"Book name: {book_object_details.book_name}")
            print(f"Book author:{book_object_details.book_author}")

if __name__ == "__main__":
    while True: main()