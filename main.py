from service.library_service import LibraryService
from database.json_database import JsonDatabase
from input_output.io_class import ConsoleIO
from core.config import FILE_PATH


def main() -> None:
    database = JsonDatabase(FILE_PATH)
    std_io = ConsoleIO()
    service = LibraryService(database, std_io)
    service.tracer()


if __name__ == "__main__":
    main()
