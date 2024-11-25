from abc import ABC, abstractmethod
from dataclasses import dataclass

from domain.entities.book import Book
from domain.entities.filters import BookFilters
from repositories.base import BaseBookRepository


@dataclass
class BaseBookService(ABC):
    repository: BaseBookRepository

    @abstractmethod
    def add_book(self, book: Book) -> Book:
        """ Добавляет книгу, возвращает добавленную книгу"""
        ...

    @abstractmethod
    def remove_book(self, book_id: str) -> Book:
        """Удаляет книгу, возвращает удаленную книгу"""
        ...

    @abstractmethod
    def update_book_status(self, book_id: str, status: str) -> Book:
        "Изменяет статус книги, возвращает книгу"
        ...

    @abstractmethod
    def get_all_books(self) -> list[Book]:
        "Возвращает все книги"
        ...

    @abstractmethod
    def get_books_by_filter(self, _filter: BookFilters) -> list[Book]:
        "Возвращает книги по фильтрам"
        ...
