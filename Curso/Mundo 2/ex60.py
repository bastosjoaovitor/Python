from math import factorial

while True:
    try:
        n = int(input(('\nDigite um número para saber seu fatorial: ')))
        break
    except ValueError:
        print('\nEntrada inválida.')

print()

print(f'{n}! = {n} ', end='')

f = factorial(n)

while not n == 1:
    n = n - 1
    print(f'x {n} ', end='')

print(f'= {f}')

print()