from dataclasses import dataclass

from domain.entities.book import Book
from domain.entities.filters import BookFilters
from repositories.base import BaseBookRepository
from repositories.js import JsonBookRepository
from .base import BaseBookService


@dataclass
class JsonBookService(BaseBookService):
    """JSON сервис работающий с JSONBookRepository"""
    repository: BaseBookRepository = JsonBookRepository

    def add_book(self, book: Book) -> Book:
        return self.repository.add_book(book)

    def remove_book(self, book_id: str) -> Book:
        return self.repository.remove_book(book_id)

    def update_book_status(self, book_id: str, status: str) -> Book:
        return self.repository.update_book_status(book_id, status)

    def get_all_books(self) -> list[Book]:
        return self.repository.get_books_by_filter(BookFilters())

    def get_books_by_filter(self, _filter: BookFilters) -> list[Book]:
        return self.repository.get_books_by_filter(_filter)

