import json
import os
from typing import List
from library import Book
from library import User

class LibraryStorage:
    """
    A class to manage storage of books and users in JSON files.

    Attributes:
        _book_file (str): Path to the JSON file storing book data.
        _user_file (str): Path to the JSON file storing user data.

    Methods:
        save_books(books: List[Book]) -> None:
            Saves a list of books to the book JSON file.

        save_users(users: List[User]) -> None:
            Saves a list of users to the user JSON file.

        load_books() -> List[Book]:
            Loads books from the book JSON file.

        load_users() -> List[User]:
            Loads users from the user JSON file.
    """

    _book_file: str
    _user_file: str

    def __init__(self, book_file: str = 'data/books.json', user_file: str = 'data/users.json') -> None:
        """
        Initializes the LibraryStorage with file paths.

        Args:
            book_file (str): Path to the book JSON file. Default is 'data/books.json'.
            user_file (str): Path to the user JSON file. Default is 'data/users.json'.
        """
        self._book_file = book_file
        self._user_file = user_file

    def save_books(self, books: List[Book]) -> None:
        """
        Saves a list of books to the book JSON file.

        Args:
            books (List[Book]): A list of books to save.
        """
        with open(self._book_file, 'w') as f:
            books_dict_list = [book.to_dict() for book in books]
            f.write(json.dumps(books_dict_list, indent=4))

    def save_users(self, users: List[User]) -> None:
        """
        Saves a list of users to the user JSON file.

        Args:
            users (List[User]): A list of users to save.
        """
        with open(self._user_file, 'w') as f:
            users_dict_list = [user.to_dict() for user in users]
            f.write(json.dumps(users_dict_list, indent=4))

    def load_books(self) -> List[Book]:
        """
        Loads books from the book JSON file.

        Returns:
            List[Book]: A list of books loaded from the file.
        """
        books: List[Book] = []
        if os.path.exists(self._book_file):
            with open(self._book_file, 'r') as f:
                books_dict_list = json.load(f)
                books = [Book.from_dict(book_dict) for book_dict in books_dict_list]
        return books

    def load_users(self) -> List[User]:
        """
        Loads users from the user JSON file.

        Returns:
            List[User]: A list of users loaded from the file.
        """
        users: List[User] = []
        if os.path.exists(self._user_file):
            with open(self._user_file, 'r') as f:
                users_dict_list = json.load(f)
                users = [User.from_dict(user_dict) for user_dict in users_dict_list]
        return users
