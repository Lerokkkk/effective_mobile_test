from api.views import add_book_view, remove_book_view, find_book_by_filter_view, find_all_books_view, \
    update_book_status_view

router = {
    '1': add_book_view,
    '2': remove_book_view,
    '3': find_book_by_filter_view,
    '4': find_all_books_view,
    '5': update_book_status_view,
}
