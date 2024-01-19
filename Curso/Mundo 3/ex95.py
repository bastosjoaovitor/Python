jogadores = []
continuar = 'S'

separador = f'{40*"="}'

print(), print(separador),print(f'{"\033[4mCadastro dos jogadores\033[m":^47}'), print(separador)

while continuar == 'S':

    jogador = {}

    while True:

        jogador['nome'] = input('\nNome do jogador: ').strip().title()
        if jogador['nome'] != '':
            break

    while True:

        try:
            jogador['partidas'] = int(input('\nPartidas jogadas: '))
            if 0 < jogador['partidas'] < 6:
                break
        except ValueError:
            print('\nEntrada inválida.')

    gols = []

    for partida in range(0,jogador['partidas']):

        while True:
            try:
                gol = int(input(f'\n  Gols na partida {partida+1}: '))
                if gol > -1:
                    gols.append(gol)
                    break
            except ValueError:
                print('\nEntrada inválida.')
        jogador['gols'] = gols

    while True:

        continuar = input('\nAdicionar outro jogador? [S/N] : ').upper().title()
        if continuar in ['S','N']:
            break
        else:
            print('\nDigite "S" ou "N".')

    jogador['total'] = sum(jogador['gols'])

    jogadores.append(jogador)

print(),print(separador), print(), print(f'{40*"-"}')

print(f'{"Cod":<4}', end=''), print(f'{" Nome":<15}', end=''), print(f'{"Gols":<15}', end=''), print(f'{"Total":<6}')
print(f'{40*"-"}')

for i, jogador in enumerate(jogadores):

    print(f'{i:<3} {jogador["nome"]:<15}{", ".join(map(str, jogador["gols"])):<15}{jogador["total"]}')

print(f'{40*"-"}')

while True:

    print(), print(separador)

    print(f'''\nOpções:
          
  [ 1 ] - Mostrar dados de jogador
  [ 2 ] - Mostrar lista
  [ 3 ] - Finalizar programa''')
    
    while True:

        opcao = input('\nOpção: ').strip().title()
        if opcao in ['1','2','3']:
            break

    if opcao == '1':

        while True:

            try:
                indice = int(input('\nDigite a posição do jogador na lista ( -1 para voltar ao menu ) : '))
                if -2 < indice < len(jogadores):
                    if indice != -1:
                        print()
                        print(jogadores[indice])
                    break
            except ValueError:
                    print('\nEntrada inválida.')
    
    elif opcao == '2':

        print(), print(f'{40*"-"}')

        print(f'{"Cod":<4}', end=''), print(f'{" Nome":<15}', end=''), print(f'{"Gols":<15}', end=''), print(f'{"Total":<6}')
        print(f'{40*"-"}')

        for i, jogador in enumerate(jogadores):

            print(f'{i:<3} {jogador["nome"]:<15}{", ".join(map(str, jogador["gols"])):<15}{jogador["total"]}')

        print(f'{40*"-"}')

    elif opcao == '3':

        from time import sleep

        print(), print(separador)

        for letra in f'\nFinalizando programa''...\n\nAdeus\n\n':

            if letra == ".":
                sleep(0.5)
                print(letra, end='', flush=True)
                sleep(0.5)
            else:
                print(letra, end='', flush=True)
                sleep(0.05)

        exit()
