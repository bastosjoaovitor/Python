a = 0
b = 0
c = []
d = 0

while True:

    a = float(input('\nDigite um número: '))

    b += 1

    c += [a]

    d += a

    confirmacao = input('\nQuer continuar? [S/N] : ')

    if confirmacao == 'N':
        break

c = sorted(c)

print(f'\nVocê digitou {b} números e a média foi {d/b}\n')

print(f'O maior valor foi {max(c)} e o menor foi {min(c)}')

print(f'\nO maior valor foi {c[b-1]} e o menor foi {c[0]}\n')