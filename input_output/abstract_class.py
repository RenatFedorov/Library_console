from abc import ABC, abstractmethod
from models.models import Book


class AbstractIO(ABC):
    """
    An abstract base class defining the interface for i/o operations.
    """

    @staticmethod
    @abstractmethod
    def clear() -> None:
        """
        Clears the console based on the operating system.
        """
        pass

    @abstractmethod
    def proceed_command(self) -> str:
        """
        Processes the input commands from the user.
        """
        pass

    @staticmethod
    @abstractmethod
    def input_title() -> str:
        """
        Prompts the user to input the title of a book.

        Returns:
            str: The title of the book.
        """
        pass

    @staticmethod
    @abstractmethod
    def input_author() -> str:
        """
        Prompts the user to input the author of a book.

        Returns:
            str: The author of the book.
        """
        pass

    @staticmethod
    @abstractmethod
    def input_year() -> str:
        """
        Prompts the user to input the publication year of a book.

        Returns:
            str: The year the book was published.
        """
        pass

    @staticmethod
    @abstractmethod
    def input_id() -> str:
        """
        Prompts the user to input the ID of a book.

        Returns:
            str: The ID of the book.
        """
        pass

    @staticmethod
    @abstractmethod
    def input_status() -> str:
        """
        Prompts the user to input the status of a book.

        Returns:
            str: The status of the book.
        """
        pass

    @staticmethod
    @abstractmethod
    def input_query() -> str:
        """
        Prompts the user to input a search query.

        Returns:
            str: The search query.
        """
        pass

    @staticmethod
    @abstractmethod
    def input_field() -> str:
        """
        Prompts the user to input a search field.

        Returns:
            str: The search field.
        """
        pass

    @abstractmethod
    def input_book(self) -> tuple | None:
        """
        Prompts the user to input the details of a book.

        Returns:
            tuple | None: The details of the book (title, author, year) or None if input is cancelled.
        """
        pass

    @abstractmethod
    def output_books(self, books: list[Book]) -> None:
        """
        Outputs the list of books to the user.

        Args:
            books (list[Book]): The list of books to output.
        """
        pass

    @staticmethod
    @abstractmethod
    def output_message(out_message: str, center: bool = False) -> None:
        """
        Outputs a message to the user.

        Args:
            out_message (str): The message to output.
            center (bool): Whether to center the message in the console.
        """
        pass

    @staticmethod
    @abstractmethod
    def input_message(in_message: str, center: bool = False) -> str:
        """
        Prompts the user to input a message.

        Args:
            in_message (str): The input prompt message.
            center (bool): Whether to center the message in the console.

        Returns:
            str: The user's input.
        """
        pass
