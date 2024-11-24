from dataclasses import dataclass
from domain.exceptions.base import ApplicationException


@dataclass(eq=False)
class BookNotFoundException(ApplicationException):
    id: str

    @property
    def message(self):
        return f'Книги с id {self.id} не существует'
