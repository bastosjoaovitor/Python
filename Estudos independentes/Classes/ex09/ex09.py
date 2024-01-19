
# Especialista - Classe Sistema de Vendas: Crie uma classe chamada Produto com atributos para nome e preço. Em seguida, crie uma classe CarrinhoDeCompras que contém uma lista de objetos Produto. Adicione métodos para adicionar produtos, remover produtos e calcular o total da compra.

class Product():

    def __init__(self, name, price):
        
        self.name = name
        self.price = price

class ShoppingCart():

    def __init__(self):

        self.cart = []

    def add_product(self, product):

        if isinstance(product, Product):
            self.cart.append(product)
    
    def remove_product(self, product):

        if product in self.cart:
            self.cart.remove(product)

    def total_price(self):
        
        total = 0
        for value in self.cart:
            total += value.price
        return total

