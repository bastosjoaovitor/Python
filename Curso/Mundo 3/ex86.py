matriz = [[],[],[]]

print('\nMATRIZ')

for c in range(0,9):

    while True:

        try:
            if c == 0:
                valor = int(input('\nDigite um número: '))
            else:
                valor = int(input('Mais um: '))
            if c in [0,1,2]:
                matriz[0].append(valor)
            elif c in [3,4,5]:
                matriz[1].append(valor)
            elif c in [6,7,8]:
                matriz[2].append(valor)
            break

        except ValueError:
            print('\nEntrada inválida.')

print(f'{40*"="}')

print(matriz[0])
print(matriz[1])
print(matriz[2])

print()