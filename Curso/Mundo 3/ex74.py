from random import randint

numeros_aleatorios = []

for a in range(5):
    numeros_aleatorios += [randint(1,10)]

tupla = tuple(numeros_aleatorios)

numeros_ordenados = sorted(tupla)

print(f'\n{tupla}\n')

print(f'O menor valor foi {numeros_ordenados[0]} e o maior foi {numeros_ordenados[4]}.\n')