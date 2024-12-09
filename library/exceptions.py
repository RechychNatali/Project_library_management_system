"""
exceptions module for the library system

Defines custom exceptions used within the library package.

Classes:
    LibraryException
    BookNotAvailableException
    UserNotRegisteredException
"""


class LibraryException(Exception):
    """Base exception for errors related to the library system."""
    pass


class BookNotAvailableException(LibraryException):
    """Raised when a user attempts to borrow a book that is already checked out."""
    pass


class UserNotRegisteredException(LibraryException):
    """Raised when an operation is attempted by an unregistered user."""
    pass
