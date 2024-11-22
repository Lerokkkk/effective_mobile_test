from dataclasses import dataclass, field

from domain.entities.book import Book
from domain.values.title import Title
from domain.values.year import Year
from repositories.book.base import BaseBookRepository


@dataclass
class MemoryBookRepository(BaseBookRepository):
    _books: list[Book] = field(
        default_factory=list,
        kw_only=True
    )

    def add_book(self, book: Book):
        self._books.append(book)
        return book

    def find_book(self):
        pass

    def get_books(self):
        pass

    def remove_book(self):
        pass


r = MemoryBookRepository()
r.add_book(Book(Title('12'), 'Пушкин', Year(1234)))