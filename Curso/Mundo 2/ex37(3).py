SEPARADOR = '\033[34m\n{:=<50}\n\033[m'

def obter_numero():
    while True:
        try:
            return int(input('\033[36mDigite um número inteiro para convertê-lo: \033[33m'))
        except ValueError:
            print('\033[31m\nEntrada inválida. Digite um número inteiro válido.\n\033[m')

def exibir_menu():
    print('\033[36mEscolha uma das opções para conversão:')
    print('[ \033[32m1\033[m \033[36m] converter para BINÁRIO')
    print('[ \033[32m2\033[m \033[36m] converter para OCTAL')
    print('[ \033[32m3\033[m \033[36m] converter para HEXADECIMAL\033[m')

def obter_opcao():
    while True:
        try:
            opcao = int(input('\033[36mSua opção: \033[32m'))
            if 1 <= opcao <= 3:
                return opcao
            else:
                print('\033[31m\nOpção inválida. Escolha uma opção válida (1, 2 ou 3).\n\033[m')
        except ValueError:
            print('\033[31m\nEntrada inválida. Digite um número inteiro válido.\n\033[m')

def realizar_conversao(numero, opcao):
    if opcao == 1:
        resultado = bin(numero)[2:]
        tipo = 'BINÁRIO'
    elif opcao == 2:
        resultado = oct(numero)[2:]
        tipo = 'OCTAL'
    else:
        resultado = hex(numero)[2:]
        tipo = 'HEXADECIMAL'
    print(f'\033[36m\nO número \033[33m{numero}\033[m \033[36mconvertido em {tipo} vira \033[33m{resultado}\033[m')

# Início do programa principal
print(SEPARADOR.format(''))
numero = obter_numero()
print(SEPARADOR.format(''))
exibir_menu()
opcao = obter_opcao()
print(SEPARADOR.format(''))
realizar_conversao(numero, opcao)
print(SEPARADOR.format(''))
