from api.router import router
from domain.exceptions.base import ApplicationException


def app():
    while True:
        try:
            print('-' * 20)
            print('1. Добавление книги')
            print('2. Удаление книги')
            print('3. Поиск книги')
            print('4. Отображение всех книг')
            print('5. Изменение статуса книги')
            request = input('Введите число ("exit" для выхода): ')
            print('-' * 20)
            if request == "exit":
                break
            else:
                router[request]()

        except ApplicationException as e:
            print('-' * 20)
            print(e.message)


if __name__ == "__main__":
    app()
