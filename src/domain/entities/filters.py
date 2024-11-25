from dataclasses import dataclass, fields


@dataclass(eq=False)
class BookFilters:
    title: str | None = None
    author: str | None = None
    year: int | None = None
