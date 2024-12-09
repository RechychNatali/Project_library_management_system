"""
Main module for the library system.

This module initializes the library system, loads existing library data, and demonstrates adding books and registering
users. It includes a sample checkout process, handles exceptions specific to library operations, and tests descriptor
functionality.

Functions:
    main(): Main function to initialize the library, load data, add books and users, test descriptor validation,
    checkout a book, and save library data.

Usage:
    Run this module directly to test library operations.
"""

from library import Book
from library import BookNotAvailableException
from library import Library
from library import LibraryException
from library import User
from library import UserNotRegisteredException


def print_exception(exception_message: str) -> None:
    control_seq_red = '\033[91m'
    control_seq_end = '\033[0m'
    print(control_seq_red + exception_message + control_seq_end)


def interactive_menu(library: Library) -> None:
    print("The library system is ready for further operations.")

    while True:
        print("Menu:")
        print("1. Add book")
        print("2. Add user")
        print("3. List books")
        print("4. List users")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        try:
            if choice == '1':
                title = input("Enter book title: ")
                author = input("Enter book author: ")

                # Simply call add_book. Library handles existing book checks internally.
                library.add_book(title, author)
                print(f"Book '{title}' added or updated successfully.")

            elif choice == '2':
                user_id = int(input("Enter user ID: "))
                name = input("Enter user name: ")

                # Simply call register_user. Library handles existing user checks internally.
                library.register_user(user_id, name)
                print(f"User with ID {user_id} added or updated successfully.")

            elif choice == '3':
                print("\nBooks in library:")
                # List all books in the library
                for book in library.get_books():
                    print(book)

            elif choice == '4':
                print("\nUsers in library:")
                # List all users in the library
                for user in library.get_users():
                    print(f"ID: {user.user_id}, Name: {user.name}")

            elif choice == '5':
                # Exit the program
                print("Exiting...")
                break

            else:
                # Invalid menu choice
                print("Invalid choice. Please try again.")

        except LibraryException as e:
            # Handle custom library exceptions
            print(f"Error: {e}")
        except ValueError:
            # Handle invalid user inputs
            print("Invalid input. Please enter correct values.")


def main():
    """
    Initialize the library system, load data, add books, register users,
    test descriptors for validation, checkout a book, and save the data.

    This function demonstrates the entire library system workflow, including
    descriptor validation for book titles, authors, and user IDs.
    """
    library = Library()

    # Load existing data
    library.load_library_data()

    # Adding books to the library
    library.add_book("Python for Beginners", "Unknown")
    library.add_book("Advanced Python", "John Doe")
    library.add_book("Data Science Essentials", "Jane Smith")
    library.add_book("Machine Learning Basics", "Emily Johnson")
    library.add_book("Deep Learning Fundamentals", "Michael Brown")

    # Registering users
    library.register_user(1, 'Maksym')
    library.register_user(2, 'Olha')
    library.register_user(3, 'Ihor')

    # Checkout a book
    try:
        library.checkout_book(1, "Python for beginners")
    except LibraryException as exp:
        print_exception(str(exp))

    # Save library data
    library.save_library_data()

    # Testing descriptors
    print("Testing descriptor validation:")

    # Valid book and user
    try:
        print("Creating valid book and user objects:")
        valid_book = Book("Python Programming", "John Doe")
        valid_user = User(1, "Alice")
        print(f"Book created: {valid_book.title} by {valid_book.author}")
        print(f"User created: ID {valid_user.user_id}, Name {valid_user.name}")
    except LibraryException as e:
        print_exception(f"Error creating valid objects: {e}")

    # Invalid book
    try:
        print("Creating invalid book object:")
        _ = Book("", "John Doe")
    except LibraryException as e:
        print_exception(f"Error: {e}")

    # Invalid user
    try:
        print("Creating invalid user object:")
        _ = User(-5, "Bob")
    except LibraryException as e:
        print_exception(f"Error: {e}")

    # Trying to check out a book
    try:
        library.checkout_book(3, "Python for Beginners")  # User not registered
    except UserNotRegisteredException as e:
        print_exception(f"Error: {e}")

    try:
        library.checkout_book(1, "Advanced Python")  # First checkout
        library.checkout_book(2, "Advanced Python")  # Second checkout
    except BookNotAvailableException as e:
        print_exception(f"Error: {e}")

    # Additional functionality for dynamic testing remains available through the menu.
    interactive_menu(library)


if __name__ == "__main__":
    main()
