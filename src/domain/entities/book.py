from enum import StrEnum
from dataclasses import dataclass, field
from uuid import uuid4

from domain.exceptions.book import WrongStatusException


class StatusEnum(StrEnum):
    in_stock = 'в наличии'
    issued = 'выдана'


@dataclass(eq=False)
class Book:
    title: str

    author: str

    year: int

    status: StatusEnum = field(
        default=StatusEnum.in_stock,
        kw_only=True
    )

    oid: str = field(
        default_factory=lambda: str(uuid4()),
        kw_only=True
    )

    def change_status(self, status):
        try:
            self.status = StatusEnum(status)
        except ValueError:
            raise WrongStatusException(status)
