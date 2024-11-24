from dataclasses import dataclass
from abc import abstractmethod, ABC

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
    def get_all_books(self) -> list[Book]:
        ...

    @abstractmethod
    def get_books_by_filter(self, _filter: dict) -> Book | list[Book]:
        ...


