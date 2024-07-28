from abc import ABC, abstractmethod
from models.models import Book


class AbstractDatabase(ABC):
    """
    A class to handle database operations for the library system.
    """

    @abstractmethod
    def load_books(self) -> list[Book]:
        """
        Loads books from a data source.

        Returns:
            List[Book]: A list of Book instances.
        """
        raise NotImplementedError()

    @abstractmethod
    def save_books(self, books: list[Book]) -> None:
        """
        Saves books to a data source.

        Args:
            books (List[Book]): A list of Book instances to be saved.
        """
        raise NotImplementedError()

    @abstractmethod
    def add_book(self, book: Book) -> None:
        """
        Adds a new book to the library.

        Args:
            book (Book): The Book instance to be added.
        """
        raise NotImplementedError()

    @abstractmethod
    def delete_book(self, book_id: str) -> bool:
        """
        Deletes a book from the library by its ID.

        Args:
            book_id (str): The ID of the book to be deleted.

        Returns:
            bool: True if the book was deleted, False if the book was not found.
        """
        raise NotImplementedError()

    @abstractmethod
    def find_books(self, query: str, field: str) -> list[Book]:
        """
        Searches for books by a specified field (title, author, or year).

        Args:
            query (str): The search query.
            field (str): The field to search by ('title', 'author', or 'year').

        Returns:
            List[Book]: A list of Book instances that match the search criteria.
        """
        raise NotImplementedError()

    @abstractmethod
    def change_book_status(self, book_id: str, new_status: str) -> bool:
        """
        Changes the status of a book by its ID.

        Args:
            book_id (str): The ID of the book.
            new_status (str): The new status of the book ('в наличии' or 'выдана').

        Returns:
            bool: True if the status was changed, False if the book was not found.
        """
        raise NotImplementedError()

    @abstractmethod
    def find_book(self, book_id: str) -> Book | None:
        """
        Finds and returns a book by its ID.

        Args:
            book_id (str): The ID of the book to find.

        Returns:
            Book: The book with the matching ID, or None if no such book exists.
        """
        raise NotImplementedError()
