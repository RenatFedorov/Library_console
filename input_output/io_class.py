import uuid
import os
from datetime import datetime as dt
from core.dependency import handle_input
from input_output.abstract_class import AbstractIO
from core.config import commands, per_page
from models.models import Book
from core.config import message, valid_fields, valid_status


class ConsoleIO(AbstractIO):
    """
    Class that handles input through the console.
    """

    @staticmethod
    def clear() -> None:
        """
        Clears the console based on the operating system.
        """
        if os.name == "posix":
            os.system("clear")
        else:
            os.system("cls")

    @handle_input(str)
    def proceed_command(self) -> str:
        """
        Processes the input commands from the user.

        Returns:
            str: The entered command.
        """
        while True:
            command: str = self.input_message(message["enter_command"]).strip().lower()
            if command in commands:
                self.clear()
                return command
            self.output_message(message["unknown_command"])

    @handle_input(str)
    def input_title(self) -> str:
        """
        Prompts the user to input the title of a book.

        Returns:
            str: The title of the book.
        """
        return self.input_message(message["enter_title"]).strip()

    @handle_input(str)
    def input_author(self) -> str:
        """
        Prompts the user to input the author of a book.

        Returns:
            str: The author of the book.
        """
        return self.input_message(message["enter_author"]).strip()

    @handle_input(int)
    def input_year(self) -> str:
        """
        Prompts the user to input the publication year of a book.

        Returns:
            str: The year the book was published.
        """
        year: str = self.input_message(message["enter_year"]).strip()
        if 1 <= int(year) <= dt.utcnow().year:
            return year
        raise ValueError(message["invalid_year"])

    @handle_input(uuid.UUID)
    def input_id(self) -> str:
        """
        Prompts the user to input the ID of a book.

        Returns:
            str: The ID of the book.
        """
        return self.input_message(message["enter_id"]).strip()

    @handle_input(str)
    def input_status(self) -> str:
        """
        Prompts the user to input the status of a book.

        Returns:
            str: The status of the book.
        """
        status: str = self.input_message(message["enter_status"]).strip().capitalize()
        if status in valid_status:
            return status
        raise ValueError(message["invalid_status"] % str(valid_status))

    @handle_input(str)
    def input_query(self) -> str:
        """
        Prompts the user to input a search query.

        Returns:
            str: The search query.
        """
        self.clear()
        return self.input_message(message["enter_keywords"]).strip().lower()

    @handle_input(str)
    def input_field(self) -> str:
        """
        Prompts the user to input the field to search by.

        Returns:
            str: The field to search by.
        """
        field: str = self.input_message(message["enter_field"]).strip().lower()
        if field in valid_fields:
            return field
        self.clear()
        raise ValueError(message["invalid_field"] % str(valid_fields))

    def input_book(self) -> tuple | None:
        """
        Prompts the user to input the details of a book.

        Returns:
            tuple | None: A tuple containing the title, author, and year of the book, or None if input is invalid.
        """
        title: str = self.input_title()
        if title is None:
            return None
        author: str = self.input_author()
        if author is None:
            return None
        year: str = self.input_year()
        if year is None:
            return None
        return title, author, year

    def output_books(self, books: list[Book]) -> None:
        """
        Outputs a list of books to the console.

        Args:
            books (list[Book]): The list of books to output.
        """
        self.clear()
        count = 1
        self.output_message(message["books_in_library"], center=True)
        try:
            for book in books:
                self.output_message("%s. %s" % (count, book))
                if (
                        count % per_page == 0
                        and (count // per_page) < len(books)
                        and book != books[-1]
                ):
                    self.input_message(message["next_page"], center=True)
                    self.clear()
                    self.output_message(message["books_in_library"], center=True)
                elif count % per_page == 0 and (count // per_page) == len(books):
                    self.input_message(message["next_page"], center=True)
                    self.clear()
                elif book == books[-1]:
                    self.input_message(message["exit"], center=True)
                    self.clear()
                count += 1
        except KeyboardInterrupt:
            return self.clear()

    @staticmethod
    def output_message(out_message: str, center: bool = False) -> None:
        """
        Outputs a message to the console.

        Args:
            out_message (str): The message to output.
            center (bool): Whether to center the message in the console.
        """
        if center:
            return print(out_message.center(os.get_terminal_size().columns))
        return print(out_message)

    @staticmethod
    def input_message(in_message: str, center: bool = False) -> str:
        """
        Prompts the user for input with a message.

        Args:
            in_message (str): The prompt message.
            center (bool): Whether to center the message in the console.

        Returns:
            str: The user input.
        """
        if center:
            return input(in_message.center(os.get_terminal_size().columns))
        return input(in_message)
