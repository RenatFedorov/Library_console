commands = ("add", "delete", "find", "list", "status", "help", "exit")
per_page = 3
lang = "ru"
FILE_PATH = "library_books.json"
valid_fields = ("author", "title", "year")
valid_status = ("В наличии", "Выдана")

MESSAGES = {
    "ru": {
        "welcome": "Добро пожаловать в систему управления библиотекой!",
        "unknown_command": "Неизвестная команда. Для списка команд введите 'help'.",
        "enter_command": "\nВведите команду: ",
        "enter_title": "\nВведите название книги: ",
        "enter_author": "\nВведите имя автора: ",
        "enter_year": "\nВведите год издания книги: ",
        "invalid_year": "Ошибка: Год издания должен быть числом от 1 до %s",
        "enter_id": "Введите id книги: ",
        "invalid_id": "Ошибка: Неверный формат ID.",
        "enter_status": "\nВведите новый статус книги: ",
        "invalid_status": "Неверный статус. Возможные значения: %s",
        "status_changed": "Статус книги успешно изменен на \"%s\"\n\n\n",
        "enter_keywords": "Введите ключевые слова: ",
        "enter_field": "По какому полю искать: ",
        "invalid_field": "Неверное поле. Возможные значения: %s",
        "books_in_library": "Книги в библиотеке:",
        "next_page": "\n\n\nСледующая страница:",
        "exit": "\n\n\nВыход:",
        "error": "Ошибка: %s",
        "no_books_found": "Нет книг, подходящих вашему запросу: %s - %s",
        "book_not_found": "Данной книги не существует.\n",
        "book_not_found_id": "Книги с данным id не существует",
        "book_deleted": "Книга успешно удалена.\n",
        "book_added": "Книга успешно добавлена в библиотеку.\n\n\n",
        "no_books": "Нет книг, подходящих вашему запросу.\n",
        "goodbye": "Всего доброго!",
        "help_message": """Доступные команды:
add - Добавить новую книгу
delete - Удалить книгу по ID
find - Найти книги по title, author или year
list - Показать все книги
status - Изменить статус книги
help - Показать доступные команды
exit - Выйти из приложения
""",
    },
}

message = MESSAGES[lang]
