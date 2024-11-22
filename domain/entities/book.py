import enum
from dataclasses import dataclass, field
from uuid import uuid4

from domain.values.title import Title
from domain.values.year import Year


class StatusEnum(enum.Enum):
    in_stock = 'в наличии'
    issued = 'выдана'


@dataclass(eq=False)
class Book:
    title: Title

    author: str

    year: Year

    status: StatusEnum = field(
        default=StatusEnum.in_stock.value,
        kw_only=True
    )

    oid: str = field(
        default_factory=lambda: str(uuid4()),
        kw_only=True
    )
