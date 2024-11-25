from dataclasses import dataclass

from api.exceptions.author import EmptyAuthorException
from api.exceptions.id import EmptyIdException
from api.exceptions.status import EmptyStatusException
from api.exceptions.title import EmptyTitleException
from datetime import datetime

from api.exceptions.year import YearTypeException, YearTooBigException, EmptyYearException
from domain.entities.book import Book
from domain.entities.filters import BookFilters


@dataclass(frozen=True)
class BookInSchema:
    title: str
    author: str
    year: int

    def validate_title(self):
        if not self.title:
            raise EmptyTitleException()

    def validate_author(self):
        if not self.author:
            raise EmptyAuthorException()

    def validate_year(self):
        if not self.year:
            raise EmptyYearException()
        if self.year > datetime.now().year:
            raise YearTooBigException(datetime.now().year)

    def __post_init__(self):
        self.validate_title()
        self.validate_author()
        self.validate_year()

    def to_entity(self):
        return Book(
            title=self.title,
            author=self.author,
            year=self.year,
        )


@dataclass(frozen=True)
class BookFiltersSchema:
    title: str | None = None
    author: str | None = None
    year: str | None = None

    def __post_init__(self):
        self.validate_year()

    def validate_year(self):
        if self.year and not self.year.isdigit():
            raise YearTypeException()

    def to_entity(self):
        return BookFilters(
            title=self.title,
            author=self.author,
            year=int(self.year) if self.year else None
        )


@dataclass(frozen=True)
class BookChangeStatusInSchema:
    id: str
    status: str

    def validate_id(self):
        if not self.id:
            raise EmptyIdException()

    def validate_status(self):
        if not self.status:
            raise EmptyStatusException()

    def __post_init__(self):
        self.validate_id()
        self.validate_status()
