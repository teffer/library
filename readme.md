### Программа представляет собой консольное приложение для управления библиотекой книг. Пользователь может добавлять книги, удалять их, искать по различным параметрам, просматривать весь каталог книг и изменять состояние книг (в наличии или выдана). Все данные хранятся я в файле books.json.
## Фнкционал приложения включает в себя:
- **Добавление книг** — добавление книги с указанием названия, автора, года издания.
- **Удаление книг** — удаление книги по ID.
- **Поиск книг** — поиск по ID, автору или году издания.
- **Просмотр всех книг** — просмотр полного списка книг.
- **Изменение статуса книги** — изменение статуса на "В наличии" или "Выдана".
- **Сохранение данных** — запись текущего состояния библиотеки в файл.
- **Выход** — завершение работы программы с возможностью сохранения данных.
## Запуск
- Для работы программы требуется python версии 3.8 или выше
- Исходный код доступен по адресу https://github.com/teffer/library
Можно скачать и запустить вручную либо склонировать с помощью команды:
```bash
git clone https://github.com/teffer/library
```
## Формат json данных
Данные хранятся ввдие 
```json
[
    {
        "id": 1,        
        "title": "qwe", 
        "author": "ewq",
        "year": 2,      
        "status": true  
    }
]
```
## Инструкция использования
После запуска main.py пользователю будет представлен выбор возможных операций
```bash
Выберите действие:
1. Добавить книгу
2. Удалить книгу
3. Найти книгу
4. Просмотреть все книги
5. Изменить статус книги
6. Сохранить данные
7. Выход
```
Далее пользователь может выбрать один из пунктов введя число интересующего его пункта, например 3
### Пример работы программы
Введите номер действия: 3
```bash
    Параметры поиска:
    1. По ID
    2. По автору
    3. По году издания

Выберите параметр поиска: 1
Введите ID книги: 1
Id - 1, Название - qwe, Автор - ewq, Год издания - 2, Статус - В наличии
```
После завершения операции пользователь будет возращён в главное меню, откуда может продолжить работу с программой или выйти.
Выход с помощью опции в меню или сочетанием клавиш ctrl+c даст возможность сохранить данные перед выходом.
### Пример 
```bash
    Выберите действие:
    1. Добавить книгу
    2. Удалить книгу
    3. Найти книгу
    4. Просмотреть все книги
    5. Изменить статус книги
    6. Сохранить данные
    7. Выход

Введите номер действия: Сохранить данные перед выходом? (Да/нет): да
Данные сохранены.
До свидания! 
```
## Обработка ошибок
Большая часть ошибок обрабатывается и уведомляет пользователя об этом.
### Ошибки ввода
При неправильном вводе, например букв в численное поле, пользователь будет уведомлён об этом и возвращён в главное меню.
#### Пример 
```bash
    Выберите действие:      
    1. Добавить книгу       
    2. Удалить книгу        
    3. Найти книгу
    4. Просмотреть все книги
    5. Изменить статус книги
    6. Сохранить данные
    7. Выход

Введите номер действия: qwe
Ошибка: нужно ввести цифру от 1 до 7.
```
### Ошибки чтения и записи данных
В случаях ошибок чтения или записи программа сразу уведомит пользователя и позволит успешно завершить процесс работы без потери данных. 
#### пример при ошибки сохранения данные можно будет вывести в виде json на экран консоли
```bash
    Выберите действие:      
    1. Добавить книгу       
    2. Удалить книгу        
    3. Найти книгу
    4. Просмотреть все книги
    5. Изменить статус книги
    6. Сохранить данные
    7. Выход

Введите номер действия: 6
Ошибка при сохранении книг в файл - 
Надо ли вывести все данные в консоль? (Да/нет)да
[
    {
        "id": 1,
        "title": "qwe",
        "author": "ewq",
        "year": 2,
        "status": true
    }
]
```
### Ошибки в ходе программы, например удаления несуществующей книги
```bash
  Выберите действие:
    1. Добавить книгу
    2. Удалить книгу
    3. Найти книгу
    4. Просмотреть все книги
    5. Изменить статус книги
    6. Сохранить данные
    7. Выход

Введите номер действия: 2
Введите ID книги для удаления: 3
Удаление книги с айди 3 невозможно, книга не сущетсвует.
```
Таким образом программа представляет собой надёжное приложения для удобной работы с каталогом книг.