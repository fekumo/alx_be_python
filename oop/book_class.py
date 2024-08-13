#!/usr/bin/env python3

class Book:
    def __init__(self, title, author, year):
        """
        Constructor that initializes a Book instance with title, author, and year.
        """
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """
        Destructor that prints a message upon object deletion.
        """
        print(f"Deleting {self.title}")

    def __str__(self):
        """
        String representation method. Returns a user-friendly string describing the book.
        """
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """
        Official representation method. Returns a string that would recreate the Book instance.
        """
        return f"Book('{self.title}', '{self.author}', {self.year})"
