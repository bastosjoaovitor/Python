
# Avançado - Polimorfismo: Crie uma classe chamada Forma com um método para calcular a área. Em seguida, crie classes para Círculo, Quadrado e Retângulo que herdam de Forma e implementam o método de cálculo da área de maneira apropriada.

from math import pi

class Form():
    
    def calculate_area(self):
        raise


class Square(Form):

    def __init__(self, side):
        self.side = side

    def calculate_area(self):
        return self.side ** 2


class Rectangle(Form):

    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        return self.base * self.height


class Triangle(Form):

    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        return ( self.base * self.height ) / 2


class Circle(Form):

    def __init__(self, ray):
        self.ray = ray

    def calculate_area(self):
        return pi * self.ray ** 2


class Cube(Form):

    def __init__(self, base):
        self.base = base

    def calculate_area(self):
        return 6 * self.base ** 2

