from dataclasses import dataclass, field

from src.domain.entities.book import Book
from src.repositories.base import BaseBookRepository


@dataclass
class MemoryBookRepository(BaseBookRepository):
    _books: list[Book] = field(
        default_factory=list,
        kw_only=True
    )

    def _find_book_by_id(self, book_id: str) -> Book:
        return next((book for book in self._books if book.oid == book_id), None)

    def add_book(self, book: Book):
        self._books.append(book)
        return book

    def get_all_books(self) -> list[Book]:
        return self._books

    def get_books_by_filter(self, _filter: dict) -> list[Book]:
        book_list = list()
        for book in self._books:
            if all(getattr(book, key) == value for key, value in _filter.items()):
                book_list.append(book)

        return book_list

    def remove_book(self, book_id: str):
        book_to_remove = self._find_book_by_id(book_id)
        self._books.remove(book_to_remove)


r = MemoryBookRepository()
a = Book('1', 'Пушкин', 1234)
b = Book('2', 'Тютчев', 2024)
r.add_book(a)
r.add_book(b)
_filter = {
}

print(*r.get_books_by_filter(_filter))
