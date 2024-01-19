
# Iniciante - Classe Carro: Crie uma classe chamada Carro com atributos para marca, modelo e ano. Adicione um método que imprima as informações do carro.

from time import sleep

carros_cadastrados = []

class Carro():

    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

def confirmar(msg, tipo = str, opcoes_limitadas = False, opcoes = 0):

    while True:

        try:
            valor = input(msg)
            if valor == '':
                print('\n\033[31mEntrada inválida.\033[m')
                continue
            if tipo == int:
                valor = int(valor)
            if opcoes_limitadas == True:
                if valor in opcoes:
                    break
                else:
                    print('\n\033[31mEntrada inválida.\033[m')
                    continue
            break
        except:
            print('\n\033[31mEntrada inválida.\033[m')
    return valor

while True:

    print()
    print(30*"=")
    print(f'{"\033[4mCarros\033[m":^37}')
    print(30*"=")

    print('''
[ 1 ] - Cadastrar carro
[ 2 ] - Mostrar carros cadastrados
[ 3 ] - Sair do programa''')
    
    opcao = confirmar('\nOpção: ', int, opcoes_limitadas= True, opcoes=[1,2,3])

    if opcao == 1:
        
        print('\nPara cadastrar seu carro, digite as seguintes informações:')

        marca = confirmar('\nMarca: ').strip()
        modelo = confirmar('\nModelo: ').strip()
        ano = confirmar('\nAno: ', int)

        carro = Carro(marca, modelo, ano)
        carros_cadastrados.append(carro)

    elif opcao == 2:

        if len(carros_cadastrados) == 0 :
            print('\nAinda nào há carros cadastrados.')
            sleep(1)
        else:
            print('\nEsses são os carros cadastrados: ')
            print()
            print(48*"-")
            print(f'{"Marca":<16}{"Modelo":^16}{"Ano":>16}')
            print(48*"-")
            for carro in carros_cadastrados:
                print(f'{carro.marca:<16}{carro.modelo:^16}{carro.ano:>16}')
            print(48*"-")
            sleep(2)

    elif opcao == 3:

        for caractere in '\nFinalizando programa...\n\nAdeus\n\n':
            print(caractere, end='', flush=True)
            if caractere == '.':
                sleep(1)
            else:
                sleep(0.04)
        break
