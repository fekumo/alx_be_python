#!/usr/bin/env python3

class Book:
    """A class to represent a generic book."""

    def __init__(self, title, author):
        """Initialize the book with a title and an author."""
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute to track whether the book is checked out

    def check_out(self):
        """Mark the book as checked out."""
        self._is_checked_out = True

    def return_book(self):
        """Mark the book as returned and available."""
        self._is_checked_out = False

    def is_available(self):
        """Return True if the book is available, False otherwise."""
        return not self._is_checked_out

    def __str__(self):
        """Return a string representation of the book."""
        return f"Book: {self.title} by {self.author}"


class Library:
    """A class to represent the library and manage its collection of books."""

    def __init__(self):
        """Initialize the library with no explicit books list."""
        self._book_store = {}  # Use a dictionary to store books by title

    def add_book(self, book):
        """Add a book to the library's collection using its title as the key."""
        if book.title in self._book_store:
            print(f"The book '{book.title}' already exists in the library.")
        else:
            self._book_store[book.title] = book

    def check_out_book(self, title):
        """Check out a book from the library by title, if available."""
        if title in self._book_store:
            book = self._book_store[title]
            if book.is_available():
                book.check_out()
                print(f"'{title}' has been checked out.")
            else:
                print(f"Sorry, '{title}' is already checked out.")
        else:
            print(f"Sorry, '{title}' is not available in the library.")

    def return_book(self, title):
        """Return a book to the library by title, if it was checked out."""
        if title in self._book_store:
            book = self._book_store[title]
            if not book.is_available():
                book.return_book()
                print(f"'{title}' has been returned.")
            else:
                print(f"'{title}' was not checked out.")
        else:
            print(f"Sorry, '{title}' is not available in the library.")

    def available_books(self):
        """Return a list of available books in the library."""
        available = [str(book) for book in self._book_store.values() if book.is_available()]
        if available:
            return available
        else:
            return ["No books are currently available."]

