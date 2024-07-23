from database.abstract_base import AbstractDatabase
from input_output.abstract_class import AbstractIO
import inspect
import sys
import os
from models.models import Book
from core.config import message, commands


class LibraryService:
    functions: dict = {}

    def __init__(self, database: AbstractDatabase, std_io: AbstractIO):
        self.database = database
        self.std_io = std_io

    def tracer(self) -> None:
        """
        Main loop for processing commands.
        """
        while True:
            self.help()
            command: str = self.std_io.proceed_command()
            if command is None:
                continue
            try:
                self.get_class_method(command)
            except KeyError:
                self.std_io.output_message(message["unknown_command"] % command)

    def get_class_method(self, key: str):
        """
        Returns and executes the method corresponding to the given command key.

        This method dynamically collects all methods of the class (except for the constructor) and
        stores them in a dictionary. If the dictionary is not already populated, it initializes
        it with method names as keys and method objects as values. It then retrieves and executes
        the method corresponding to the provided key.

        Args:
            key (str): The command key corresponding to the method to be executed.

        Returns:
            Any: The result of the executed method.

        Raises:
            KeyError: If the provided key does not match any method name.
        """
        if not self.functions:
            methods: list = inspect.getmembers(self, predicate=inspect.ismethod)
            self.functions: dict = {method[0]: method[1] for method in methods if method[0] in commands}
        return self.functions[key]()

    def add(self) -> None:
        """
        Adds a new book to the library.
        """
        if info := self.std_io.input_book():
            self.std_io.clear()
            book: Book = Book(*info)
            self.database.add_book(book)
            self.std_io.output_message(message["book_added"], center=True)

    def delete(self) -> None:
        """
        Deletes a book from the library by ID.
        """
        book_id: str = self.std_io.input_id()
        if not book_id:
            return None
        self.std_io.clear()
        if self.database.delete_book(book_id):
            return self.std_io.output_message(message["book_deleted"], center=True)
        self.std_io.output_message(message["book_not_found"], center=True)

    def find(self) -> None:
        """
        Finds books by title, author or year.
        """
        query: str = self.std_io.input_query()
        if not query:
            return None
        field: str = self.std_io.input_field()
        if not field:
            return None
        books: list[Book] = self.database.find_books(query, field)
        if books:
            return self.std_io.output_books(books)
        self.std_io.output_message(message["no_books_found"] % (field, query))

    def list(self) -> None:
        """
        Lists all books in the library.
        """
        self.std_io.clear()
        books: list[Book] = self.database.load_books()
        if books:
            return self.std_io.output_books(books)
        self.std_io.output_message(message["no_books"])

    def status(self) -> None:
        """
        Changes the status of a book by ID.
        """
        book_id: str = self.std_io.input_id()
        if not book_id:
            return None
        self.std_io.clear()
        if self.database.find_book(book_id) is None:
            return self.std_io.output_message(message["book_not_found_id"])
        new_status: str = self.std_io.input_status()
        if new_status:
            self.database.change_book_status(book_id, new_status)
            self.std_io.clear()
            self.std_io.output_message(message["status_changed"] % new_status, center=True)

    def help(self) -> None:
        """
        Displays the list of available commands.
        """
        self.std_io.clear()
        self.std_io.output_message(message["welcome"], center=True)
        self.std_io.output_message(message["help_message"])

    def exit(self) -> None: # noqa
        """
        Exits the application.
        """
        sys.exit(message["goodbye"].center(os.get_terminal_size().columns))
