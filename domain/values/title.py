from dataclasses import dataclass

from domain.exceptions.title import EmptyTitleException
from domain.values.base import BaseValueObject


@dataclass(frozen=True)
class Title(BaseValueObject):
    value: str

    def validate(self):
        if not self.value:
            raise EmptyTitleException()

    def as_generic_type(self) -> str:
        return str(self.value)

