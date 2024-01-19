
# Avançado - Classe Livraria: Crie uma classe chamada Livro com atributos para título, autor e preço. Em seguida, crie uma classe Livraria que contém uma lista de objetos Livro. Adicione métodos para adicionar livros, remover livros e encontrar livros por autor.


class Book():

    def __init__(self, name, author, literary_genre, price):

        self.name = name
        self.author = author
        self.literary_genre = literary_genre
        self.price = f'US${price:.2f}'


class Shelf():

    def __init__(self, author):

        self.books = []
        self.number_of_books = len(self.books)
        self.author = author

    def add_book(self, book):

        if isinstance(book, Book):
            if book.author == self.author:
                self.books.append(book)
                self.number_of_books += 1

    def remove_book(self, book):
        
        if book in self.books:
            self.books.remove(book)
            self.number_of_books -= 1


class Library():
    
    def __init__(self, name):

        self.name = name
        self.shelfs = {}
        self.number_of_shelves = len(self.shelfs)

    def add_shelf(self, shelf):

        permission = True
        for value in self.shelfs.values():
            if shelf == value:
                permission = False
            if permission == True:
                if isinstance(shelf, Shelf):
                    if shelf.author not in self.shelfs:
                        self.shelfs[f'{shelf.author}'] = shelf
                        self.number_of_shelves += 1

    def remove_shelf(self, shelf):

        if shelf in self.shelfs.values():
            self.shelfs.pop(shelf, None)
            self.number_of_shelves -= 1

