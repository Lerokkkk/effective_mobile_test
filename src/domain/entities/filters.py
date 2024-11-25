from dataclasses import dataclass, fields


@dataclass(eq=False)
class BookFilters:
    """Объект фильтров для поиска книги"""
    title: str | None = None
    author: str | None = None
    year: int | None = None
