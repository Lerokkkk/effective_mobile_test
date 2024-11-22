from dataclasses import dataclass
from domain.exceptions.base import ApplicationException


@dataclass(eq=True)
class YearTooBigException(ApplicationException):
    year: int

    @property
    def message(self):
        return f'{self.year} год еще не наступил'
