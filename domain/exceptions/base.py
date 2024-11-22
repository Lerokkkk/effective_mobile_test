from dataclasses import dataclass


@dataclass(eq=True)
class ApplicationException(Exception):
    @property
    def message(self):
        return 'Произошла ошибка приложения'
