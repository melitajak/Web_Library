class Book:
    def __init__(self, id, title, author, reader_id=None, library_id=None):
        self.id = id
        self.title = title
        self.author = author

books = [
    Book(1, "Book 1", "Author 1"),
    Book(2, "Book 2", "Author 2"),
    Book(3, "Book 3", "Author 3"),
]
