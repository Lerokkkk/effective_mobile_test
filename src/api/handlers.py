from api.schemas import BookInSchema, BookFiltersSchema, BookChangeStatusInSchema
from dto.book import BookDTO
from services.base import BaseBookService


def add_book_handler(book_input: BookInSchema, service: BaseBookService):
    """Хэндлер для добавления книги"""
    book_entity = service.add_book(book_input.to_entity())
    return BookDTO.from_entity(book_entity)


def remove_book_handler(book_id: str, service: BaseBookService):
    """Хэндлер для удаления книги"""
    return BookDTO.from_entity(service.remove_book(book_id))


def find_book_by_filter_handler(filters: BookFiltersSchema, service: BaseBookService):
    """Хэндлер для вывода книг по фильтрам"""
    response_from_service = service.get_books_by_filter(filters.to_entity())

    return [BookDTO.from_entity(obj) for obj in response_from_service]


def find_all_books_handler(service: BaseBookService):
    """Хэндлер для вывода всех книг"""
    response_from_service = service.get_all_books()
    return [BookDTO.from_entity(obj) for obj in response_from_service]


def update_book_status_handler(book: BookChangeStatusInSchema, service: BaseBookService):
    """Хэндлер для изменения статуса книги"""
    book_entity = service.update_book_status(book.id, book.status)

    return BookDTO.from_entity(book_entity)
