numeros = [[],[]]

print('\nDigite 7 valores, direi quais são pares e quais são ímpares.')

for c in range(0,7):

    while True:

        try:
            if c == 0:
                valor = int(input('\nDigite um valor: '))
            else:
                valor = int(input('\nMais um: '))
            if valor % 2 == 0:
                numeros[0].append(valor)
            else:
                numeros[1].append(valor)
            break

        except ValueError:
            print('\nEntrada inválida, para saber se um número é par ou não, digite um número inteiro')

print(f'\nOs números pares são {numeros[0]} e os números ímpares são {numeros[1]}\n')