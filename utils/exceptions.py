from typing import Optional


class MappedException(Exception):
    def __init__(self, status_code: int, message: str, error_code: Optional[str] = None):
        self.status_code = status_code
        self.message = message
        self.error_code = error_code
        super().__init__(self.message)
