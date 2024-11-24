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


# try:
#     b = Book('123', 'Пушкин', 2024)
#     b.change_status('сдача')
#
# except WrongStatusException as e:
#     print(e.message)
# except ValueError as e:
#     print(e)
