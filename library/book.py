"""
book module for the library system

Defines the Book class, which represents a book with properties such as title,
author, and a checkout status. Provides methods to check out and return the book.

Classes:
    Book: Represents a single book in the library system.

Methods:
    checkout(): Marks the book as checked out, raising an exception if it's already checked out.
    return_book(): Marks the book as returned, raising an exception if it's already returned.
    title: Returns the title of the book.
    author: Returns the author of the book.
"""
from typing import Dict

from .descriptors import AuthorDescriptor
from .descriptors import TitleDescriptor
from .exceptions import BookNotAvailableException
from .exceptions import LibraryException


class Book:
    title = TitleDescriptor()
    author = AuthorDescriptor()
    _is_checked_out: bool

    def __init__(self, title: str, author: str) -> None:
        """
                Initializes a Book instance with a title, an author, and a default checked-out status.

                Args:
                    title (str): The title of the book.
                    author (str): The author of the book.
                """
        self.title = title
        self.author = author
        self._is_checked_out = False

    def checkout(self) -> None:
        """
               Marks the book as checked out if it is not already checked out.

               Raises:
                   BookNotAvailableException: If the book is already checked out.
               """
        if not self._is_checked_out:
            self._is_checked_out = True
        else:
            raise BookNotAvailableException(f"Book {str(self)} is already checked out")

    def return_book(self) -> None:
        """
               Marks the book as returned if it is currently checked out.

               Raises:
                   LibraryException: If the book is already returned.
               """
        if self._is_checked_out:
            self._is_checked_out = False
        else:
            raise LibraryException("Book is not checked out")

    def __str__(self) -> str:
        return f"{self.title} by {self.author}"

    def to_dict(self) -> Dict[str, str]:
        return {"title": self.title, "author": self.author}

    @classmethod
    def from_dict(cls: "Book", input_dict: Dict[str, str]) -> "Book":
        title = input_dict["title"].strip()
        author = input_dict["author"].strip()
        return Book(title, author)
