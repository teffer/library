import os
import sys
import library as lb
import book as bk
import msvcrt

def display_menu():
    print("""
    Выберите действие:
    1. Добавить книгу
    2. Удалить книгу
    3. Найти книгу
    4. Просмотреть все книги
    5. Изменить статус книги
    6. Сохранить данные
    7. Выход
    """)

def add_book(library):
    try:
        title: str = input("Введите название книги: ")
        author: str = input("Введите автора книги: ")
        year: int = int(input("Введите год издания: "))
        book = bk.Book(0, title, author, year, True) 
        # id будет присвоенно автоматически при добавлении экземпляра в список книг,
        # если id книги в списке 0 будет означать что произошла ошибка при добавлении книги,
        # но данные самой книги не будут утеряны
        library.add(book)
    except ValueError:
        print("Некорректный ввод данных. Повторите попытку.")

def delete_book(library):
    try:
        id = int(input("Введите ID книги для удаления: "))
        print(library.delete(id))
    except ValueError:
        print("Некорректный ввод ID. Повторите попытку.")

def find_book(library):
    print("""
    Параметры поиска:
    1. По ID
    2. По автору
    3. По году издания
    """)
    try:
        choice = int(input("Выберите параметр поиска: "))
        if choice == 1:
            id = int(input("Введите ID книги: "))
            books = library.find(id)
        elif choice == 2:
            author = input("Введите автора книги: ")
            books = library.find(author)
        elif choice == 3:
            year = int(input("Введите год издания книги: "))
            books = library.find(year)
        else:
            print("Неверный выбор.")
            return
        if books:
            for book in books:
                print(book)
        else:
            print("Книги не найдены.")
    except ValueError:
        print("Некорректный ввод. Повторите попытку.")

def view_all_books(library):
    books = library.find_all()
    if books:
        for book in books:
            print(book)
    else:
        print("В библиотеке пока нет книг.")

def change_book_status(library):
    try:
        id = int(input("Введите ID книги: "))
        new_status = input("Книга на данный момент в библиотеке? (Да/нет): ").strip().lower() == "да"
        print(library.change_status(id, new_status))
    except ValueError:
        print("Некорректный ввод данных. Повторите попытку.")

def safe_exit(library):
    if input("Сохранить данные перед выходом? (Да/нет): ").strip().lower() == "да":
        library._save_data()
    print("До свидания!")
    sys.exit()

def main():
    library_path = "books.json"
    library = lb.Library(library_path)
    while True:
        display_menu()
        try:
            choice = int(input("Введите номер действия: "))
            if choice == 1:
                add_book(library)
            elif choice == 2:
                delete_book(library)
            elif choice == 3:
                find_book(library)
            elif choice == 4:
                view_all_books(library)
            elif choice == 5:
                change_book_status(library)
            elif choice == 6:
                library._save_data()
            elif choice == 7:
                safe_exit(library)
            else:
                print("Неверный выбор. Повторите попытку.")
            input("\nНажмите Enter, чтобы продолжить...")
            os.system('cls||clear')
        except ValueError:
            print("Ошибка: нужно ввести цифру от 1 до 7.")
            input("\nНажмите Enter, чтобы продолжить...")
            os.system('cls||clear')
        except KeyboardInterrupt:
            safe_exit(library)
        except Exception as e:
            print(f"\nПроизошла ошибка: {e}")
            input("\nНажмите Enter, чтобы продолжить...")
            os.system('cls||clear')

if __name__ == "__main__":
    main()