STATUS_VAL = { True: 'В наличии', False: 'Выдана', None: 'Неизвестно'}
class Book():
    def __init__(self, id: int, title: str, author: str, year: int, status: bool) -> None:
        self.id = id
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    def covert_to_dict(self) -> list:
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "status": self.status,
        }
    
    @staticmethod
    def from_dict(data: list) -> 'Book':
        return Book(
            id=data["id"],
            title=data["title"],
            author=data["author"],
            year=data["year"],
            status=data["status"],
        )
    
    def __str__(self):
        return f'Id - {self.id}, Название - {self.title}, Автор - {self.author}, Год издания - {self.year}, Статус - {STATUS_VAL[self.status]}'