from dataclasses import dataclass

from src.dto.exceptions.title import EmptyTitleException
from src.dto.schemas.base import BaseValueObject


@dataclass(frozen=True)
class Title(BaseValueObject):
    value: str

    def validate(self):
        if not self.value:
            raise EmptyTitleException()

    def as_generic_type(self) -> str:
        return str(self.value)

