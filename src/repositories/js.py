import json
from dataclasses import dataclass

from domain.exceptions.book import WrongStatusException
from dto.book import BookDTO
from repositories.exceptions.book import BookNotFoundException
from src.domain.entities.book import Book, StatusEnum
from settings.config import JSON_FILE
from domain.exceptions.base import ApplicationException


@dataclass
class JsonBookRepository():

    def _load_books(self) -> list[BookDTO]:
        with open(JSON_FILE, 'r', encoding='utf-8') as file:
            try:
                load_data = json.load(file)
                data = [BookDTO.from_dict(obj) for obj in load_data]
                return data
            except json.JSONDecodeError:
                raise ApplicationException()

    def _save_books(self, data: list[BookDTO]):
        valid_data = [obj.to_dict() for obj in data]
        with open(JSON_FILE, 'w', encoding='utf-8') as file:
            json.dump(valid_data, file, ensure_ascii=False, indent=4)

    def _find_book_with_index_by_id(self, book_id: str, data: list[BookDTO]):
        for index, book in enumerate(data):
            if book.oid == book_id:
                return index, book
        raise BookNotFoundException(book_id)

    def add_book(self, book: Book) -> Book:
        try:
            data = self._load_books()
        except ApplicationException:
            data = list()
        new_book = BookDTO.from_entity(book)
        data.append(new_book)
        self._save_books(data)

        return new_book.to_entity()

    def remove_book(self, book_id: str) -> Book:
        data = self._load_books()
        found_index, found_book = self._find_book_with_index_by_id(book_id, data)
        data.remove(found_book)
        self._save_books(data)
        return found_book.to_entity()

    def update_book_status(self, book_id: str, status: str) -> Book:
        data = self._load_books()
        found_index, found_book = self._find_book_with_index_by_id(book_id, data)
        book_entity = found_book.to_entity()

        book_entity.change_status(status)
        book_dto = BookDTO.from_entity(book_entity)
        data[found_index] = book_dto
        return book_entity

    def get_books(self, _filter: dict) -> list[Book]:
        response_book_list = list()
        data = self._load_books()
        for book in data:
            if all(getattr(book, key) == value for key, value in _filter.items()):
                response_book_list.append(book.to_entity())

        return response_book_list


r = JsonBookRepository()
print(r.get_books({}))