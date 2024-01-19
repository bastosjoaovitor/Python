lista = []
lista_pares = []
lista_impares = []
separador = f'{40*"=-"}='

while True:
    
    while True:

        try:
            valor = int(input('\nDigite um valor: '))
            lista.append(valor)
            break
        except ValueError:
            print('\nEntrada inválida.')

    while True:
        
        try:
            fim = input('\nAdicionar mais um valor [S/N] : ').strip().upper()
            if fim != '':
                fim = fim[0]
            if fim in ['S','Y','N']:
                break
        except ValueError:
            print('\nEntrada inválida.')

    if fim == 'N':
        break

for numero in lista:
    if numero % 2 == 0:
        lista_pares.append(numero)
    else:
        lista_impares.append(numero)

print('\n',separador,'\n')

print(f'Essa é a lista na ordem que você digitou: {lista}\n')
print(f'Esses são os números pares digitados: {lista_pares}\n')
print(f'Esses são os números ímpares digitados: {lista_impares}')

print('\n',separador,'\n')