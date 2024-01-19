
# Intermediário - Herança de Classes: Crie uma classe chamada Animal com atributos para nome e idade. Em seguida, crie uma classe Cachorro que herda de Animal e adiciona um atributo para raça.

class Animal():

    def __init__(self, name, age, weight, diet, habitat) :

        self.name = name
        self.age = int(age)
        self.weight = float(weight)
        self.diet = diet
        self.habitat = habitat

class Dog(Animal):

    def __init__(self, name, age, weight, diet, habitat, breed):

        super().__init__(name, age, weight, diet, habitat)
        self.breed = breed

animals = {}

dog = Dog('Cachorro', 1, 80, 'Carnívoro', 'Planeta', 'Pitbull')
animals['Dogs'] = dog

print(f'''
Name: {animals['Dogs'].name}
Age: {animals['Dogs'].age} {'year' if animals['Dogs'].age == 1 else 'years'}
weight: {animals['Dogs'].weight}
diet: {animals['Dogs'].diet}
habitat: {animals['Dogs'].habitat}
breed: {animals['Dogs'].breed}
''')