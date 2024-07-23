import uuid
from dataclasses import dataclass, asdict


@dataclass
class Book:
    """
    Represents a book in the library.

    Attributes:
        title (str): The title of the book.
        author (str): The author of the book.
        year (int): The year the book was published.
        id (str): The unique identifier for the book, generated automatically.
        status (str): The status of the book, either "available" or "borrowed".
    """

    title: str
    author: str
    year: int
    id: str = str(uuid.uuid4())
    status: str = "В наличии"

    def __str__(self):
        return f"Book: {self.title}({self.author}), {self.year}, status: {self.status}. (id:{self.id})"

    def to_dict(self) -> dict:
        """
        Converts the Book instance to a dictionary.

        Returns:
            dict: A dictionary representation of the Book instance.
        """
        return asdict(self)

    @staticmethod
    def from_dict(data: dict) -> "Book":
        """
        Creates a Book instance from a dictionary.

        Args:
            data (dict): A dictionary containing the book information.

        Returns:
            Book: A Book instance created from the dictionary data.
        """
        return Book(**data)
