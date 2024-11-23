import json
import os
import sys
import book as bk

STATUS_VAL = { True: 'В наличии', False: 'Выдана', None: 'Неизвестно'}

class Library():
    def __init__(self,books_data_path: str) -> None:
        self.books: list = self.load_from_json(books_data_path)
        self.data_file = books_data_path

    def load_from_json(self, path)->list:
        if not os.path.exists(path):
            print(f"Файл {path} не найден. Данные будут сохранены в новый файл.") 
            return [] 
            # Так как расположения файла не меняется по ходу работы с библиотекой можно гарантировать,
            # что будет создан новый файл по указанному пути,
            # а старый файл, даже если он существует останется нетронутым
        try:
            with open(path, 'r', encoding='utf-8') as f:
                books_data = json.load(f)
                books = [bk.Book.from_dict(book) for book in books_data]
                return books
        except Exception as e:
            # в случае если файл был повреждён (например вручную удалена скобка), 
            # файл не будет считываться корректно, и если продолжить работу, сохранение добавленных элементов перезапишет все данные.
            print(f'Ошибка при попытке считать данные из файла - {e}')
            if input('Нужно ли продолжить работу программы, есть риск потерять данные библиотеки (Да/нет)').strip().lower() == 'да':
                if input('Вы уверенны? (Да, нет)').strip().lower() == 'да':
                    return []
            sys.exit()
        
    def _save_data(self) -> None:
        try:
            raise Exception
            with open(self.data_file, "w", encoding="utf-8") as f:
                json.dump([book.covert_to_dict() for book in self.books], f, indent=4, ensure_ascii=False)
                print("Данные сохранены.")
        except Exception as e:
            # случай когда сохранение в файл недоступно, например у пользователя нет прав для создания или записи в файлы,
            # то будет можно сохранить данные скопировав из консоли
            print(f'Ошибка при сохранении книг в файл - {e}')
            if input('Надо ли вывести все данные в консоль? (Да/нет)').strip().lower() == 'да':
                print(json.dumps([book.covert_to_dict() for book in self.books], indent=4, ensure_ascii=False))
                input("\nНажмите Enter, чтобы продолжить...")

    def add(self, book:bk.Book)->None:
        if book is not None:
            try:
                # генерация нового айдишника, всегда увеличивается, что гарантирует уникальность, неважно сколько элементов быдет удалено.
                # так как допускается гипотетическая возможность нескольких книг с айди 0 то тут ошибки не будет
                self.next_id: int = max((book.id for book in self.books), default=0) + 1
                book.id = self.next_id
                self.books.append(book)
                print(f'Книга {book} успешно добавлена в библиотеку')
            except Exception as e:
                print(f'Ошибка при добавлении книги - {e}')
        else: print(f'Ошибка при добавлении книги - невозможно вставить пустую книгу')


    def delete(self, id:int)->str:
        try:
            book:bk.Book = next((book for book in self.books if book.id == id), None)
            if book is not None:
                self.books.remove(book)
                return f'Удаление книги {book} прошло успешно'
            else:
                return f'Удаление книги с айди {id} невозможно, книга не сущетсвует.'
        except Exception as e: 
            return f'Ошибка при удалении книги - {e}'
        
    def find(self,id:int = None, author:str = '',year:str = '')->list:
        try:
            temp_book_selection = []
            if id is not None:
                for book in self.books:
                    if book.id == id:
                        temp_book_selection.append(book)
                return temp_book_selection
            elif author != '':
                for book in self.books:
                    if book.author == author:
                        temp_book_selection.append(book)
                return temp_book_selection
            elif year != '':
                for book in self.books:
                    if book.year == year:
                        temp_book_selection.append(book)
                return temp_book_selection
            else: 
                # если что то пошло не так и фронт не поймал ошибку в аргументах для поиска, возрващён будет пустой список при любом раскладе
                print(f'Параметры для поиска книги указаны не верно или не указаны вовсе.')
                return temp_book_selection
        except Exception as e:
            print(f'Ошибка при поике книги - {e}')
            return []
    
    def find_all(self) -> list:
        try:
            return self.books
        except Exception as e:
            print(f'Ошибка при выводе все книг - {e}')
            return []
        
    def change_status(self, id: int, new_status:bool) -> str:
        try:
            book: bk.Book = next((book for book in self.books if book.id == id), None)
            if book is not None:                   
                book.status = new_status
                return f'Статус книги изменён на {STATUS_VAL[new_status]}'
            else: return f'Изменение статуса книги с айди {id} невозможно, книга не сущетсвует.'
        except Exception as e:
            return f'Ошибка при изменении статуса книги - {e}'
        