from functools import wraps
from datetime import datetime as dt
from uuid import UUID

from core.config import message


def handle_input(input_type=str):
    """
    Decorator to handle user input with KeyboardInterrupt checking.

    Args:
        input_type (type): Expected input type (str, int, or UUID).
    Returns:
        function: Wrapped function.
    """

    def decorator(func):
        @wraps(func)
        def wrapper(self):
            while True:
                try:
                    value = func(self)
                    if input_type == int:
                        int(value)
                    elif input_type == UUID:
                        UUID(value)
                    if not value:
                        continue
                    return value
                except ValueError as ex:

                    if input_type == int:
                        print(message["invalid_year"] % str(dt.utcnow().year))
                    elif input_type == UUID:
                        print(message["invalid_id"])
                    else:
                        print(message["error"] % ex)
                except KeyboardInterrupt:
                    self.clear()
                    break

        return wrapper

    return decorator
