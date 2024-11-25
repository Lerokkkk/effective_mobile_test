import json
from dataclasses import dataclass, fields

from domain.entities.filters import BookFilters
from dto.book import BookDTO
from repositories.base import BaseBookRepository
from repositories.exceptions.book import BookNotFoundException
from src.domain.entities.book import Book
from settings.config import JSON_FILE
from domain.exceptions.base import ApplicationException


@dataclass
class JsonBookRepository(BaseBookRepository):
    """Реализация базового репозитория для работы с JSON файлами"""

    def _conventer_filter_entity_to_dict(self, _filter: BookFilters) -> dict:
        """Метод для преобразования BookFilters в словарь"""
        query = dict()
        for field in fields(_filter):
            if getattr(_filter, field.name) is not None:
                query[field.name] = getattr(_filter, field.name)

        return query

    def _load_books(self) -> list[BookDTO]:
        """Метод для загрузки JSON файла и преобразования объектов в BookDTO"""
        with open(JSON_FILE, 'r', encoding='utf-8') as file:
            try:
                load_data = json.load(file)
                data = [BookDTO.from_dict(obj) for obj in load_data]
                return data
            except json.JSONDecodeError:
                raise ApplicationException()

    def _save_books(self, data: list[BookDTO]):
        """Метод для сохранения JSON файла"""
        valid_data = [obj.to_dict() for obj in data]
        with open(JSON_FILE, 'w', encoding='utf-8') as file:
            json.dump(valid_data, file, ensure_ascii=False, indent=4)

    def _find_book_with_index_by_id(self, book_id: str, data: list[BookDTO]):
        """Метод находит книгу и индекс книги в списке книг"""
        for index, book in enumerate(data):
            if book.oid == book_id:
                return index, book
        raise BookNotFoundException(book_id)

    def add_book(self, book: Book) -> Book:
        """Метод для добавления книги в JSON файл"""
        try:
            data = self._load_books()
        except ApplicationException:
            data = list()
        new_book = BookDTO.from_entity(book)
        data.append(new_book)
        self._save_books(data)

        return new_book.to_entity()

    def remove_book(self, book_id: str) -> Book:
        """Метод для удаления книги из JSON файла"""
        data = self._load_books()
        found_index, found_book = self._find_book_with_index_by_id(book_id, data)
        data.remove(found_book)
        self._save_books(data)
        return found_book.to_entity()

    def update_book_status(self, book_id: str, status: str) -> Book:
        """Метод для изменения статуса книги и сохранения в JSON файл"""
        data = self._load_books()
        found_index, found_book = self._find_book_with_index_by_id(book_id, data)
        book_entity = found_book.to_entity()

        book_entity.change_status(status)
        book_dto = BookDTO.from_entity(book_entity)
        data[found_index] = book_dto
        self._save_books(data)
        return book_entity

    def get_books_by_filter(self, _filter: BookFilters) -> list[Book]:
        """Метод для получения книг по фильтрам
        С пустыми полями в BookFilters выводит все книги"""
        response_book_list = list()
        data = self._load_books()
        filters = self._conventer_filter_entity_to_dict(_filter)
        for book in data:
            if all(getattr(book, key) == value for key, value in filters.items()):
                response_book_list.append(book.to_entity())

        return response_book_list
