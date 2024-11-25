from dataclasses import dataclass

from domain.exceptions.base import ApplicationException


@dataclass(eq=False)
class EmptyIdException(ApplicationException):
    @property
    def message(self):
        return 'Id книги не может быть пустым'
