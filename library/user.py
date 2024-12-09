"""
user module for the library system

Defines the User class, representing a user with the ability to borrow and return books.
Tracks the books currently checked out by the user.

Classes:
    User: Represents a library user with a unique ID, name, and a list of checked-out books.

Methods:
    borrow_book(book: Book): Checks out a book to the user and adds it to their list of borrowed books.
    return_book(book: Book): Returns a book to the library, removing it from the user's borrowed list.
    user_id: Returns the unique identifier of the user.
    name: Returns the name of the user.
"""
from typing import Dict
from typing import List
from typing import Union

from .book import Book
from .descriptors import UserIDDescriptor
from .exceptions import LibraryException


class User:
    user_id = UserIDDescriptor()
    _name: str
    _checked_out_books: List[Book]

    def __init__(self, user_id: int, name: str) -> None:
        """
               Initializes a User instance with a unique ID, name, and an empty list of checked-out books.

               Args:
                   user_id (int): Unique identifier for the user.
                   name (str): Name of the user.
               """
        self.user_id = user_id
        self._name = name
        self._checked_out_books = []

    def borrow_book(self, book: Book) -> None:
        """
               Checks out a book to the user and adds it to the user's list of checked-out books.

               Args:
                   book (Book): The book to be checked out by the user.

               Raises:
                   LibraryException: If the book is already checked out by another user.
               """
        if len(self._checked_out_books) >= 3:
            raise LibraryException("Cannot borrow more than 3 books")
        book.checkout()
        self._checked_out_books.append(book)

    def return_book(self, book: Book) -> None:
        """
                Returns a checked-out book to the library, removing it from the user's list.

                Args:
                    book (Book): The book to be returned by the user.

                Raises:
                    LibraryException: If the book is not found in the user's list of checked-out books.
                """
        if book in self._checked_out_books:
            book.return_book()
            self._checked_out_books.remove(book)
        else:
            raise LibraryException("Book not found in user's borrowed list")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name: str):
        self._name = new_name

    @property
    def checked_out_books(self):
        return self._checked_out_books

    def to_dict(self) -> Dict[str, Union[int, str]]:
        return {"user_id": self.user_id, "name": self._name}

    @classmethod
    def from_dict(cls: "User", input_dict: Dict[str, Union[int, str]]) -> "User":
        user_id = int(input_dict["user_id"])
        name = input_dict["name"].strip()
        return User(user_id, name)
