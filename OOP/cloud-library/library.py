"""
Library Management System
-to add Books's informations
-to update number of available copies for each books
-adding books to library
-check available books in library
"""

class Book:
    def __init__(self, title, author, genre, available_copies):
        self.title = title
        self.author = author
        self.genre = genre
        self.available_copies = available_copies

    def display_book(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nGenre: {self.genre}\nAvailable_copies: {self.available_copies}\n"
    
    #to update available_copies for specific book
    def update_book(self, new_available_copies):
        self.available_copies = new_available_copies
    
class Library(Book):
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        self.books.remove(book)

    def checkout_book(self, book):
        if book.available_copies > 0:
            book.available_copies -= 1
            print(f"{book.title} checked out successfully.")
        else:
            print(f"No available copies of {book.title}")

    def return_book(self, book):
        book.available_copies += 1
        print(f"{book.title} returned successfully.")

    def display_list(self):
        for book in self.books:
            print(book.display_book())

#creating instances of the book class
book1 = Book('The Hobbit', 'J.R.R. Tolkien', 'Fantasy', 6)
book2 = Book('To Kill a Mockingbird', 'Harper Lee', 'Fiction', 4)
book3 = Book('1984', 'George Orwell', 'Science Fiction', 2)

#creating instance of the library class
library = Library()

#adding books to library
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

library.checkout_book(book1)
library.checkout_book(book3)
library.checkout_book(book3)

library.display_list()