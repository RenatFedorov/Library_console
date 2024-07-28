import unittest
from unittest.mock import patch
from input_output.io_class import ConsoleIO
from core.config import commands


class TestConsoleIO(unittest.TestCase):

    @patch("builtins.input", side_effect=commands)
    def test_proceed_command_add(self, mock_input):
        console_io = ConsoleIO()
        with patch("input_output.io_class.ConsoleIO.clear"):
            for command in commands:
                output: str = console_io.proceed_command()
                self.assertEqual(output, command)

    @patch("builtins.input", return_value="Test Title")
    def test_input_title(self, mock_input):
        console_io = ConsoleIO()
        title = console_io.input_title()
        self.assertEqual(title, "Test Title")

    @patch("builtins.input", return_value="Test Author")
    def test_input_author(self, mock_input):
        console_io = ConsoleIO()
        author = console_io.input_author()
        self.assertEqual(author, "Test Author")

    @patch("builtins.input", return_value="2000")
    def test_input_year(self, mock_input):
        console_io = ConsoleIO()
        with patch("input_output.io_class.ConsoleIO.clear"):
            year = console_io.input_year()
        self.assertEqual(year, "2000")

    @patch("builtins.input", return_value="123e4567-e89b-12d3-a456-426614174000")
    def test_input_id(self, mock_input):
        console_io = ConsoleIO()
        book_id = console_io.input_id()
        self.assertEqual(book_id, "123e4567-e89b-12d3-a456-426614174000")

    @patch("builtins.input", return_value="В наличии")
    def test_input_status(self, mock_input):
        console_io = ConsoleIO()
        with patch("input_output.io_class.ConsoleIO.clear"):
            status = console_io.input_status()
        self.assertEqual(status, "В наличии")

    @patch("builtins.input", return_value="test query")
    def test_input_query(self, mock_input):
        console_io = ConsoleIO()
        query = console_io.input_query()
        self.assertEqual(query, "test query")

    @patch("builtins.input", return_value="title")
    def test_input_field(self, mock_input):
        console_io = ConsoleIO()
        with patch("input_output.io_class.ConsoleIO.clear"):
            field = console_io.input_field()
        self.assertEqual(field, "title")

    @patch("builtins.input", side_effect=["Test Title", "Test Author", "2000"])
    def test_input_book(self, mock_input):
        console_io = ConsoleIO()
        book_info = console_io.input_book()
        self.assertEqual(book_info, ("Test Title", "Test Author", "2000"))

    @patch("builtins.print")
    def test_output_message(self, mock_print):
        console_io = ConsoleIO()
        console_io.output_message("Test Message")
        mock_print.assert_called_once_with("Test Message")

    @patch("builtins.input", return_value="Test Input")
    def test_input_message(self, mock_input):
        console_io = ConsoleIO()
        message = console_io.input_message("Test Input")
        self.assertEqual(message, "Test Input")


if __name__ == "__main__":
    unittest.main()
