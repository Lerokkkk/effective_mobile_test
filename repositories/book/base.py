from dataclasses import dataclass
from abc import abstractmethod, ABC

from domain.entities.book import Book


@dataclass
class BaseBookRepository(ABC):

    @abstractmethod
    def add_book(self, book: Book):
        ...

    @abstractmethod
    def remove_book(self, book_id: int):
        ...

    @abstractmethod
    def find_book(self, ):
        ...

    @abstractmethod
    def get_books(self):
        ...

