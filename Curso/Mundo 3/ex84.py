terminar_programa = "N"

a = 0
lista = []

while terminar_programa == "N":

    while True:
        try:
            nome = input('\nDigite o nome: ')
            if nome != '':
                bloco = [nome]
                break
            else:
                print('\nEntrada inválida.')
        except ValueError:
            print('\nEntrada inválida.')

    while True:
        try:
            peso = float(input('\nPeso: '))
            if peso > 0:
                peso = peso
                bloco.append(peso)
                break
            else:
                print('\nEntrada inválida.')
        except ValueError:
            print('\nEntrada inválida.')

    a += 1
    lista.append(bloco[:])

    while True:
        try:
            terminar_programa = input('\nTerminar programa[S/N]: ')
            if terminar_programa != '':
                terminar_programa = terminar_programa[0].upper()
                if terminar_programa in ['S', 'Y', 'N']:
                    break
                else:
                    print('\nEntrada inválida.')
        except ValueError:
            print('\nEntrada inválida.')

nome_segunda_pessoa_mais_pesada = ''
peso_segunda_pessoa_mais_pesada = 0
nome_terceira_pessoa_mais_pesada = ''
peso_terceira_pessoa_mais_pesada = 0

for pessoa in lista:

    if pessoa == lista[0]:
        nome_pessoa_mais_pesada = pessoa[0]
        peso_pessoa_mais_pesada = pessoa[1]

    else:

        if pessoa[1] > peso_pessoa_mais_pesada:
            nome_terceira_pessoa_mais_pesada = nome_segunda_pessoa_mais_pesada
            peso_terceira_pessoa_mais_pesada = peso_segunda_pessoa_mais_pesada
            nome_segunda_pessoa_mais_pesada = nome_pessoa_mais_pesada
            peso_segunda_pessoa_mais_pesada = peso_pessoa_mais_pesada
            nome_pessoa_mais_pesada = pessoa[0]
            peso_pessoa_mais_pesada = pessoa[1]

        elif pessoa[1] > peso_segunda_pessoa_mais_pesada:
            nome_terceira_pessoa_mais_pesada = nome_segunda_pessoa_mais_pesada
            peso_terceira_pessoa_mais_pesada = peso_segunda_pessoa_mais_pesada
            nome_segunda_pessoa_mais_pesada = pessoa[0]
            peso_segunda_pessoa_mais_pesada = pessoa[1]

        elif pessoa[1] > peso_terceira_pessoa_mais_pesada:
            nome_terceira_pessoa_mais_pesada = pessoa[0]
            peso_terceira_pessoa_mais_pesada = pessoa[1]

print(f'\nA pessoa mais pesada é {nome_pessoa_mais_pesada} com {peso_pessoa_mais_pesada:.1f}kg.')
if nome_segunda_pessoa_mais_pesada != '':
    print(f'\nA segunda pessoa mais pesada é {nome_segunda_pessoa_mais_pesada} com {peso_segunda_pessoa_mais_pesada}kg.')
    if nome_terceira_pessoa_mais_pesada != '':
        print(f'\nE a terceira pessoa mais pesada é {nome_terceira_pessoa_mais_pesada} com {peso_terceira_pessoa_mais_pesada}kg.')

print('\nPrograma finalizado\n')