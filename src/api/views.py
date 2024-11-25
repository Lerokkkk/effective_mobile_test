from api.exceptions.year import YearTypeException
from api.handlers import add_book_handler, remove_book_handler, update_book_status_handler, find_all_books_handler, \
    find_book_by_filter_handler
from api.schemas import BookInSchema, BookFiltersSchema, BookChangeStatusInSchema
from repositories.js import JsonBookRepository
from services.js import JsonBookService

"""Файл с представлениями, конвертирующий пользовательский ввод в DTO и вызывающий сервисы"""


def add_book_view():
    try:
        title = input('Введите название книги: ')
        author = input('Введите автора книги: ')
        year = int(input('Введите год издания книги: '))

        book_in_schema = BookInSchema(title=title, author=author, year=year)
        service = JsonBookService(JsonBookRepository())

        response = add_book_handler(book_in_schema, service)
        print(f'Добавлена книга: {response}')

    except ValueError:
        raise YearTypeException()


def remove_book_view():
    book_id = input('Введите id книги: ')
    service = JsonBookService(JsonBookRepository())

    print(f'Удалена книга {remove_book_handler(book_id, service)}')


def update_book_status_view():
    book_id = input('Введите id книги: ')
    status = input('Введите статус книги ["в наличии", "выдана"]: ')

    book_in_schema = BookChangeStatusInSchema(id=book_id, status=status)
    service = JsonBookService(JsonBookRepository())

    print(f'Обновлен статус у книги: {update_book_status_handler(book_in_schema, service)}')


def find_all_books_view():
    service = JsonBookService(JsonBookRepository())
    print('Найденные книги:')
    [print(i) for i in find_all_books_handler(service)]


def find_book_by_filter_view():
    try:
        title = input('Введите название книги (для пропуска нажмите Enter): ')
        author = input('Введите автора книги (для пропуска нажмите Enter): ')
        year = input('Введите год издания книги (для пропуска нажмите Enter): ')

        book_in_schema = BookFiltersSchema(title=title if title else None,
                                           author=author if author else None,
                                           year=year if year else None)
        service = JsonBookService(JsonBookRepository())
        print('Найденные книги:')
        [print(i) for i in find_book_by_filter_handler(book_in_schema, service)]
    except ValueError:
        raise YearTypeException()
