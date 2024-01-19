print(f'\n{40*"="}')
print(f'{"BANCO PYTHON":^40}')
print(f'{40*"="}\n')

cedulas_de_50 = 0
cedulas_de_20 = 0
cedulas_de_10 = 0
cedulas_de_1 = 0

while True:
    try:
        valor = int(input('Digite o valor a ser sacado: R$'))
        if valor < 1:
            print('\nO VALOR A SER SACADO NÃO PODE SER MENOR QUE 1 REAL.\n')
        else:
            break
    except ValueError:
        print('\nENTRADA INVÁLIDA.\n')

cedulas_de_50 = valor/50
cedulas_de_50 = int(cedulas_de_50)

valor = valor - (cedulas_de_50*50)

cedulas_de_20 = valor/20
cedulas_de_20 = int(cedulas_de_20)

valor = valor - (cedulas_de_20*20)

cedulas_de_10 = valor/10
cedulas_de_10 = int(cedulas_de_10)

valor = valor - (cedulas_de_10*10)

cedulas_de_1 = valor

print(f'\nTotal de {cedulas_de_50} cédulas de R$50\nTotal de {cedulas_de_20} cédulas de R$20\nTotal de {cedulas_de_10} cédulas de R$10\nTotal de {cedulas_de_1} cédulas de R$1\n')

print(f'{40*"="}\n')

print('Tenha um bom dia! Volte sempre!\n')