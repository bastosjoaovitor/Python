
# Iniciante - Classe Pessoa: Crie uma classe chamada Pessoa que tenha atributos para nome e idade. Crie um método que imprima o nome e a idade da pessoa.

def confirmar(msg, tipo = str):

    while True:

        try:
            valor = input(msg)
            if valor == '':
                print('\033[31mEntrada inválida.\033[m')
                continue
            if tipo == int:
                valor = int(valor)
            return valor
        except:
            print('\n\033[31mEntrada inválida.\033[m')

class Pessoa():

    def __init__(self, nome, idade, sexo):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo

print()
print(30*"=")
print(f'{"\033[4mCadastre-se aqui\033[m":^37}')
print(30*"=")

nome = confirmar('\nDigite seu nome: ')

idade = confirmar('\nDigite sua idade: ', int)

while True:
    sexo = confirmar('\nDigite seu sexo [M/F] : ').upper()[0]
    if sexo in 'MF':
        break

pessoa1 = Pessoa(nome, idade, sexo)

print(f'''
Nome: {pessoa1.nome}
Idade: {pessoa1.idade}
Sexo: {pessoa1.sexo}
''')