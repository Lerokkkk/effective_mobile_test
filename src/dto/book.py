from dataclasses import dataclass

from src.domain.entities.book import Book, StatusEnum


@dataclass
class BookDTO:
    """Data Transfer Object книги для передачи между слоями приложения"""
    title: str
    author: str
    year: int
    status: str
    oid: str

    def __str__(self):
        return f'Id: {self.oid}, Название: {self.title}, Автор: {self.author}, Год: {self.year}, Статус: {self.status}'

    def __repr__(self):
        return f'Id: {self.oid}, Название: {self.title}, Автор: {self.author}, Год: {self.year}, Статус: {self.status}'

    @staticmethod
    def from_entity(book: Book) -> 'BookDTO':
        return BookDTO(title=book.title,
                       author=book.author,
                       year=book.year,
                       status=str(book.status.value),
                       oid=book.oid
                       )

    def to_entity(self) -> Book:
        return Book(title=self.title,
                    author=self.author,
                    year=self.year,
                    status=StatusEnum(self.status),
                    oid=self.oid
                    )

    def to_dict(self) -> dict:
        dict_book = {
            'title': self.title,
            'author': self.author,
            'year': self.year,
            'status': self.status,
            'oid': self.oid
        }
        return dict_book

    @staticmethod
    def from_dict(d: dict) -> 'BookDTO':
        return BookDTO(
            title=d['title'],
            author=d['author'],
            year=d['year'],
            status=d['status'],
            oid=d['oid']
        )
