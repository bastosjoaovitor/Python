a = [int(input('\nDigite um número: '))]
a += [int(input('Digite outro número: '))]
a += [int(input('Digite mais um número: '))]
a += [int(input('Digite o último número: '))]

tupla = tuple(a)

print(f'\nVocê digitou os valores {tupla}\n')

print(f'O valor 9 apareceu {tupla.count(9)} vezes.\n')

if 3 in tupla:
    print(f'O primeiro 3 que você digitou esta na posição {tupla.index(3)}.\n')
else:
    print(f'Você não digitou o número 3.\n')

pares = 0
for c in range(0,4):
    b = tupla[c] % 2
    if b == 0:
        pares += 1

print(f'Você digitou {pares} números pares.\n')