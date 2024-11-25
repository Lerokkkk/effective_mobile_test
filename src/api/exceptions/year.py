from dataclasses import dataclass

from domain.exceptions.base import ApplicationException


@dataclass(eq=False)
class YearTypeException(ApplicationException):
    @property
    def message(self):
        return 'Год должен быть целым числом'


@dataclass(eq=False)
class YearTooBigException(ApplicationException):
    current_year: int

    @property
    def message(self):
        return f'Год не может быть больше нынешнего года - {self.current_year}'


@dataclass(eq=False)
class EmptyYearException(ApplicationException):
    @property
    def message(self):
        return f'Год не может быть пустым полем'
