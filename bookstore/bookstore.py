class Bookstore(object):
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        
    def get_books(self):
        return self.books
        
    def search_books(self, title = None, author = None):
        
        book_list = []
        
        if title:
            for book in self.books:
                if title.lower() in book.get_title().lower():
                    book_list.append(book)
                    
        elif author:
            for book in self.books:
                if author == book.author:
                    book_list.append(book)
        return book_list


class Author(object):
    def __init__(self, name, nationality):
        self.name = name
        self.nationality = nationality
        self.books = []

    def get_books(self):
        return self.books
    
    def add_book(self, book):
        self.books.append(book)

class Book(object):
    def __init__(self, title, author):
        author.add_book(self)
        self.title = title
        self.author = author
        
    def get_title(self):
        return self.title