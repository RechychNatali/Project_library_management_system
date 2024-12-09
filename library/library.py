from typing import List

from .book import Book
from .exceptions import BookNotAvailableException
from .exceptions import LibraryException
from .exceptions import UserNotRegisteredException
from .storage import LibraryStorage
from .user import User


class Library:
    def __init__(self):
        self._books = []
        self._users = []
        self._storage = LibraryStorage()

    def add_book(self, title: str, author: str):
        self._books.append(Book(title, author))

    def register_user(self, user_id: int, name: str):
        self._users.append(User(user_id, name))

    def update_book_author(self, title: str, new_author: str):
        """Update the author of a book by its title."""
        book = next((book for book in self._books if book.title == title), None)
        if not book:
            raise LibraryException(f"Book with title '{title}' was not found")
        book.author = new_author
        print(f"Updated book: {title}, new author: {new_author}")

    def update_user_name(self, user_id: int, new_name: str):
        """Update the name of a user by their ID."""
        user = next((user for user in self._users if user.user_id == user_id), None)
        if not user:
            raise LibraryException(f"User with ID {user_id} was not found")
        user.name = new_name
        print(f"Updated user ID {user_id}, new name: {new_name}")

    def remove_book(self, title: str):
        """Remove a book from the library by its title."""
        book = next((book for book in self._books if book.title == title), None)
        if not book:
            raise BookNotAvailableException(f"Book with title '{title}' was not found")
        self._books.remove(book)
        print(f"Removed book: {title}")

    def remove_user(self, user_id: int):
        """Remove a user from the library by their ID."""
        user = next((user for user in self._users if user.user_id == user_id), None)
        if not user:
            raise UserNotRegisteredException(f"User with ID {user_id} was not found")
        self._users.remove(user)
        print(f"Removed user ID {user_id}")

    def checkout_book(self, user_id: int, book_title: str):
        """Check out a book to a user."""
        user: User
        book: Book
        user = next((user for user in self._users if user.user_id == user_id), None)
        book = next((book for book in self._books if book.title == book_title), None)
        if not user:
            raise UserNotRegisteredException(f"User with ID {user_id} is not registered.")
        if not book:
            raise BookNotAvailableException(f"The book '{book_title}' is not available for checkout.")

        if len(user.checked_out_books) >= 3:
            raise LibraryException(f"User {user.name} has reached the book limit")

        user.borrow_book(book)

    def save_library_data(self):
        self._storage.save_books(self._books)
        self._storage.save_users(self._users)

    def load_library_data(self):
        self._books = self._storage.load_books()
        self._users = self._storage.load_users()

    def get_books(self) -> List[Book]:
        return self._books

    def get_users(self) -> List[User]:
        return self._users
