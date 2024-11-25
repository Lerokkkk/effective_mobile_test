from dataclasses import dataclass
from abc import abstractmethod, ABC

from domain.entities.filters import BookFilters
from src.domain.entities.book import Book


@dataclass
class BaseBookRepository(ABC):

    @abstractmethod
    def add_book(self, book: Book):
        ...

    @abstractmethod
    def remove_book(self, book_id: str):
        ...

    @abstractmethod
    def get_books_by_filter(self, _filter: BookFilters) -> list[Book]:
        ...

    @abstractmethod
    def update_book_status(self, book_id: str, status: str) -> Book:
        ...
