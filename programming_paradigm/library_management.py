#!/usr/bin/env python3


class Book:
    """A class to represent a book in the library."""

    def __init__(self, title, author):
        """Initialize the book with a title and author, and set its status as available."""
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute to track availability

    def check_out(self):
        """Mark the book as checked out."""
        self._is_checked_out = True

    def return_book(self):
        """Mark the book as returned and available."""
        self._is_checked_out = False

    def is_available(self):
        """Return True if the book is available, False otherwise."""
        return not self._is_checked_out

class Library:
    """A class to represent the library and manage its collection of books."""

    def __init__(self):
        """Initialize the library with an empty list of books."""
        self._books = []

    def add_book(self, book):
        """Add a book to the library's collection."""
        self._books.append(book)

    def check_out_book(self, title):
        """Check out a book from the library by title. Mark it as checked out if available."""
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                print(f"'{title}' has been checked out.")
                return
        print(f"Sorry, '{title}' is either not in the library or already checked out.")

    def return_book(self, title):
        """Return a book to the library by title. Mark it as available if it was checked out."""
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                print(f"'{title}' has been returned.")
                return
        print(f"Sorry, '{title}' is either not in the library or wasn't checked out.")

    def list_available_books(self):
        """List all available books in the library."""
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            for book in available_books:
                print(f"{book.title} by {book.author}")
        else:
            print("No books are currently available.")

