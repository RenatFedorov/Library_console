import unittest
import os
from models.models import Book
from database.json_database import JsonDatabase


class TestJsonDatabase(unittest.TestCase):
    def setUp(self):
        self.file_path = "test_library.json"
        self.database = JsonDatabase(self.file_path)
        self.book1 = Book(
            id="1", title="Book 1", author="Author 1", year=2000, status="В наличии",
        )
        self.book2 = Book(
            id="2", title="Book 2", author="Author 2", year=2010, status="Выдана",
        )

    def tearDown(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_load_books_empty(self):
        self.assertEqual(self.database.load_books(), [])

    def test_save_and_load_books(self):
        self.database.save_books([self.book1, self.book2])
        loaded_books = self.database.load_books()
        self.assertEqual(len(loaded_books), 2)
        self.assertEqual(loaded_books[0].id, "1")
        self.assertEqual(loaded_books[1].id, "2")

    def test_add_book(self):
        self.database.add_book(self.book1)
        self.database.add_book(self.book2)
        loaded_books = self.database.load_books()
        self.assertEqual(len(loaded_books), 2)
        self.assertEqual(loaded_books[0].title, "Book 1")
        self.assertEqual(loaded_books[1].title, "Book 2")

    def test_delete_book(self):
        self.database.add_book(self.book1)
        self.assertTrue(self.database.delete_book("1"))
        self.assertFalse(self.database.delete_book("1"))
        self.assertEqual(self.database.load_books(), [])

    def test_find_books(self):
        self.database.save_books([self.book1, self.book2])
        found_books = self.database.find_books("Book 1", "title")
        self.assertEqual(len(found_books), 1)
        self.assertEqual(found_books[0].title, "Book 1")

    def test_display_books(self):
        self.database.save_books([self.book1, self.book2])
        displayed_books = self.database.load_books()
        self.assertEqual(len(displayed_books), 2)

    def test_change_book_status(self):
        self.database.save_books([self.book1])
        self.assertTrue(self.database.change_book_status("1", "Выдана"))
        updated_book = self.database.find_book("1")
        self.assertEqual(updated_book.status, "Выдана")
        self.assertFalse(self.database.change_book_status("2", "В наличии"))

    def test_find_book(self):
        self.database.save_books([self.book1])
        found_book = self.database.find_book("1")
        self.assertEqual(found_book.id, "1")
        self.assertIsNone(self.database.find_book("2"))


if __name__ == "__main__":
    unittest.main()
