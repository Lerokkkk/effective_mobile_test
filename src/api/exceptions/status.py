from dataclasses import dataclass

from domain.exceptions.base import ApplicationException


@dataclass(eq=False)
class EmptyStatusException(ApplicationException):
    @property
    def message(self):
        return 'Статус не может быть пустым'
