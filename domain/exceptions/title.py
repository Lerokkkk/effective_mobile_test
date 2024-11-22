from dataclasses import dataclass

from domain.exceptions.base import ApplicationException


@dataclass(eq=False)
class EmptyTitleException(ApplicationException):
    @property
    def message(self):
        return 'Название не может быть пустым'
