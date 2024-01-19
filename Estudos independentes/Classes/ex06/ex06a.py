
# Avançado - Classe Livraria: Crie uma classe chamada Livro com atributos para título, autor e preço. Em seguida, crie uma classe Livraria que contém uma lista de objetos Livro. Adicione métodos para adicionar livros, remover livros e encontrar livros por autor.

'''
class Shelf():

    def __init__(self, books):

        self.books = books
        self.number_of_books = len(books)
'''

class Book():

    def __init__(self, name, author, literary_genre, price):

        self.name = name
        self.author = author
        self.literary_genre = literary_genre
        self.price = f'US${price:.2f}'


class Shelf():

    def __init__(self, books):

        if isinstance(books, list) == False:
            raise Exception('\nThe "books" parameter must be filled with a list.')
        self.books = books
        self.number_of_books = len(books)

    def add_book(self, book):

        if isinstance(book, Book) == True:
            self.books.append(book)

    def remove_book(self, book):
        
        if book in self.books:
            self.books.remove(book)


class Library():
    
    def __init__(self, name):

        self.name = name
        self.shelfs = {}
        self.number_of_shelves = len(self.shelfs)

    