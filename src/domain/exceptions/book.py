from dataclasses import dataclass

from domain.exceptions.base import ApplicationException


@dataclass(eq=False)
class WrongStatusException(ApplicationException):
    status: str

    @property
    def message(self):
        return f"'{self.status}' статуса не существует"
