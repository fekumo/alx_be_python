#!/usr/bin/env python3

class Book:
    def __init__(self, title, author):
        """
        Base class constructor that initializes the title and author of a book.
        """
        self.title = title
        self.author = author

    def __str__(self):
        """
        String representation of the book, showing the title and author.
        """
        return f"Book: {self.title} by {self.author}"

class EBook(Book):
    def __init__(self, title, author, file_size):
        """
        Constructor for EBook, which inherits from Book and adds file_size.
        """
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        """
        String representation of the eBook, including the file size.
        """
        return f"EBook: {self.title} by {self.author}, File size: {self.file_size}KB"

class PrintBook(Book):
    def __init__(self, title, author, page_count):
        """
        Constructor for PrintBook, which inherits from Book and adds page_count.
        """
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        """
        String representation of the print book, including the page count.
        """
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"

class Library:
    def __init__(self):
        """
        Library class constructor that initializes an empty list of books.
        """
        self.books = []

    def add_book(self, book):
        """
        Adds a book (Book, EBook, or PrintBook instance) to the library's collection.
        """
        self.books.append(book)

    def list_books(self):
        """
        Lists all books in the library by printing their details.
        """
        for book in self.books:
            print(book)
