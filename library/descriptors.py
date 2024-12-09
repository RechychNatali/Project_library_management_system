import re
from .exceptions import LibraryException


class TitleDescriptor:
    """
    Descriptor to validate the title of a book.

    Ensures that the title is a non-empty string and does not
    contain special characters.
    """
    def __set_name__(self, owner, name):
        """
        Assigns the internal attribute name for the descriptor.

        Args:
            owner (type): The class owning the descriptor.
            name (str): The name of the attribute being managed.
        """
        self.name = f"_{name}"

    def __get__(self, instance, owner):
        """
        Retrieves the value of the managed attribute.

        Args:
            instance: The instance of the class using the descriptor.
            owner: The class type of the instance.

        Returns:
            str: The value of the title attribute.
        """
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        """
        Sets the value of the managed attribute.

        Args:
            instance: The instance of the class using the descriptor.
            value (str): The new value for the title.

        Raises:
            LibraryException: If the value is invalid.
        """
        if not value or not isinstance(value, str):
            raise LibraryException("Title must be a non-empty string.")
        if re.search(r"[^\w\s]", value):  # Checks for special characters.
            raise LibraryException("Title must not contain special characters.")
        setattr(instance, self.name, value)


class AuthorDescriptor:
    """
    Descriptor to validate the author of a book.

    Ensures that the author is a non-empty string.
    """
    def __set_name__(self, owner, name):
        """
        Assigns the internal attribute name for the descriptor.

        Args:
            owner (type): The class owning the descriptor.
            name (str): The name of the attribute being managed.
        """
        self.name = f"_{name}"

    def __get__(self, instance, owner):
        """
        Retrieves the value of the managed attribute.

        Args:
            instance: The instance of the class using the descriptor.
            owner: The class type of the instance.

        Returns:
            str: The value of the author attribute.
        """
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        """
        Sets the value of the managed attribute.

        Args:
            instance: The instance of the class using the descriptor.
            value (str): The new value for the author.

        Raises:
            LibraryException: If the value is invalid.
        """
        if not value or not isinstance(value, str):
            raise LibraryException("Author must be a non-empty string.")
        setattr(instance, self.name, value)


class UserIDDescriptor:
    """
    Descriptor to validate the user ID.

    Ensures that the user ID is a positive integer.
    """
    def __set_name__(self, owner, name) -> None:
        """
        Assigns the internal attribute name for the descriptor.

        Args:
            owner (type): The class owning the descriptor.
            name (str): The name of the attribute being managed.
        """
        self.name = f"_{name}"

    def __get__(self, instance, owner):
        """
        Retrieves the value of the managed attribute.

        Args:
            instance: The instance of the class using the descriptor.
            owner: The class type of the instance.

        Returns:
            int: The value of the user ID attribute.
        """
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        """
        Sets the value of the managed attribute.

        Args:
            instance: The instance of the class using the descriptor.
            value (int): The new value for the user ID.

        Raises:
            LibraryException: If the value is invalid.
        """
        if not isinstance(value, int) or value <= 0:
            raise LibraryException("User ID must be a positive integer.")
        setattr(instance, self.name, value)
