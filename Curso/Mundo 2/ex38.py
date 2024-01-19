separador = f'\033[34m\n{25*"-="}-\n\033[m'

print(separador)

while True:
    try:
        valor_1 = float(input('\033[36mDigite o primeiro valor: \033[33m'))
        break
    except ValueError:
        print('\033[31m\nEntrada inválida\n\033[m')

while True:
    try:
        valor_2 = float(input('\033[36m\nDigite o segundo valor: \033[33m'))
        break
    except ValueError:
        print('\033[31m\nEntrada inválida\033[m')

while True:
    try:
        valor_3 = float(input('\033[36m\nDigite o terceiro valor: \033[33m'))
        break
    except ValueError:
        print('\033[31m\nEntrada inválida\033[m')

print(separador)

if valor_1 == valor_2 and valor_2 == valor_3:
    print('\033[33mOs três valores sãos iguais.')
elif valor_1 > valor_2 and valor_2 == valor_3:
    print('\033[33mO primeiro valor é o maior e o segundo e terceiro valor são iguais.')
elif valor_1 < valor_2 and valor_2 == valor_3:
    print('\033[33mO primeiro valor é o menor e o segundo e terceiro valor são iguais.')
elif valor_2 > valor_1 and valor_1 == valor_3:
    print('\033[33mO segundo valor é o maior e o primeiro e terceiro valor são iguais.')
elif valor_2 < valor_1 and valor_1 == valor_3:
    print('\033[33mO segundo valor é o menor e o primeiro e terceiro valor são iguais.')
elif valor_3 > valor_1 and valor_1 == valor_2:
    print('\033[33mO terceiro valor é o maior e o primeiro e segundo valor são iguais.')
elif valor_3 < valor_1 and valor_1 == valor_2:
    print('\033[33mO terceiro valor é o menor e o primeiro e segundo valor são iguais.')
elif valor_1 > valor_2 and valor_2 > valor_3:
    print('\033[33mO primeiro valor é o maior e o terceiro é o menor.')
elif valor_1 > valor_3 and valor_3 > valor_2:
    print('\033[33mO primeiro valor é o maior e o segundo é o menor.')
elif valor_2 > valor_1 and valor_1 > valor_3:
    print('\033[33mO segundo valor é o maior e o terceiro é o menor')
elif valor_2 > valor_3 and valor_3 > valor_1:
    print('\033[33mO segundo valor é o maior e o terceiro é o primeiro é o menor.')
elif valor_3 > valor_1 and valor_1 > valor_2:
    print('\033[33mO terceiro valor é o maior e o primeiro é o menor.')
elif valor_3 > valor_2 and valor_2 > valor_1:
    print('\033[33mO terceiro valor é o maior e o primeiro é o menor.')

print(separador)