a = 0
lista = []

while a != 5:
    try:
        if a > 0:
            n = int(input('\nMais um: '))
            lista.append(n)
        else: 
            n = int(input('\nDigite um valor: '))
            lista.append(n)
        a += 1
    except ValueError:
        print('\nEntrada inválida.')

lista = sorted(lista)

print(f'\nO maior valor dos números digitados é {lista[4]} e o menor é {lista[0]}.\n')