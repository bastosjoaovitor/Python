lista = []

while True:

    while True:
        try:
            valor = int(input('\nDigite um valor: '))
            if valor in lista:
                print('\nVocê ja digitou esse número, valor não adicionado.')
            else:
                lista.append(valor)
            break
        except ValueError:
            print('\nEntrada inválida.')

    while True:    
        try:
            a = input('\nDigitar outro valor [S/N] : ').upper().strip()    
            if a == '':
                a = 'a'
            if a[0] in ['S','Y','N']:
                break
            else:
                print('\nDigite "S" para sim ou "N" para não.')
        except ValueError:
            print('\nEntrada inválida.')

    if a == 'N':
        lista = sorted(lista)
        break

print(f'\n{50*"="}\n')
print(lista, '\n')