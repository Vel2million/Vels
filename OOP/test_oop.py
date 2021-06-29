class Book:

    TYPES = ['hardcover', 'paperback']

    def __init__(self, name, type, weight):
        self.name = name
        self.type = type
        self.weight = weight

    def __repr__(self) -> str:
        return f"<Book {self.name}, {self.type}, {self.weight}g>"

    @classmethod
    def hardcover(cls, name, weight):
        return Book(name, Book.TYPES[0], weight + 100)


book = Book.hardcover("SHIT", 1000)
print(book)