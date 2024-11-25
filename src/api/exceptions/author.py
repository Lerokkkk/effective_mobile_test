from dataclasses import dataclass

from domain.exceptions.base import ApplicationException


@dataclass(eq=False)
class EmptyAuthorException(ApplicationException):
    @property
    def message(self):
        return 'Автор не может быть пустым'
