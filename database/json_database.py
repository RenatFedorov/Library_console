import json
from models.models import Book
from database.abstract_base import AbstractDatabase


class JsonDatabase(AbstractDatabase):
    """
    A class to handle database operations for the library system using JSON file storage.
    """

    def __init__(self, file_path: str):
        self.file_path = file_path

    def load_books(self) -> list[Book]:
        """
        Loads books from a JSON file.

        Returns:
            List[Book]: A list of Book instances.
        """
        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                data = json.load(file)
                return [Book.from_dict(book) for book in data]
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_books(self, books: list[Book]) -> None:
        """
        Saves books to a JSON file.

        Args:
            books list[Book]: A instance of Book to be saved.
        """
        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(
                [book.to_dict() for book in books], file, ensure_ascii=False, indent=4,
            )

    def add_book(self, book: Book) -> None:
        """
        Adds a new book to the library.

        Args:
            book (Book)
        """
        books = self.load_books()
        books.append(book)
        self.save_books(books)

    def delete_book(self, book_id: str) -> bool:
        """
        Deletes a book from the library by its ID.

        Args:
            book_id (str): The ID of the book to be deleted.

        Returns:
            bool: True if the book was deleted, False if the book was not found.
        """
        books = self.load_books()
        updated_books = [book for book in books if book.id != book_id]
        if len(books) == len(updated_books):
            return False
        self.save_books(updated_books)
        return True

    def find_books(self, query: str, field: str) -> list[Book]:
        """
        Searches for books by a specified field (title, author, or year).

        Args:
            query (str): The search query.
            field (str): The field to search by ('title', 'author', or 'year').

        Returns:
            List[Book]: A list of Book instances that match the search criteria.
        """
        books = self.load_books()
        return [book for book in books if str(query).lower() in str(getattr(book, field)).lower()]

    def change_book_status(self, book_id: str, new_status: str) -> bool:
        """
        Changes the status of a book by its ID.

        Args:
            book_id (str): The ID of the book.
            new_status (str): The new status of the book ('в наличии' or 'выдана').

        Returns:
            bool: True if the status was changed, False if the book was not found.
        """
        books = self.load_books()
        for book in books:
            if book.id == book_id:
                book.status = new_status
                self.save_books(books)
                return True
        return False

    def find_book(self, book_id: str) -> Book | None:
        """
        Finds and returns a book by its ID.

        Args:
            book_id (str): The ID of the book to find.

        Returns:
            Book: The book with the matching ID, or None if no such book exists.
        """
        books = self.load_books()
        for book in books:
            if book.id == book_id:
                return book
        return None
