from dataclasses import dataclass
from datetime import datetime

from domain.exceptions.year import YearTooBigException
from domain.values.base import BaseValueObject


@dataclass(frozen=True)
class Year(BaseValueObject):
    value: int

    def validate(self):
        if self.value > datetime.now().year:
            print(datetime.now().year)
            raise YearTooBigException(self.value)

    def as_generic_type(self):
        return int(self.value)