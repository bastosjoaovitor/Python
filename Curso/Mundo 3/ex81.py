lista = []
a = 0

while True:
    
    try:
        valor = int(input('\nDigite um número: '))
        lista.append(valor)
        a += 1
    except ValueError:
        print('\nEntrada inválida.')

    while True:
        fim = input('\nAdicionar mais um valor [S/N] : ').upper().strip()
        if fim != '':
            fim = fim[0]
        if fim in ['S','Y','N']:
            break

    if fim == 'N':
        break

lista.sort(reverse=True)
print()

print(f'{30*"="}\n\n{a} números foram digitados\n\nEstá é a lista organizada de forma decrescente: {lista}\n')
if 5 in lista:
    print('O valor 5 foi digitado\n')
else:
    print('O valor 5 não foi digitado.\n')