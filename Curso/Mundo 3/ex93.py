dados = {}
gols = []
total_de_gols = 0
from time import sleep

separador = f"{40*"="}"

print(), print(separador)

while True:

    dados['nome'] = input('\nNome do jogador: ')
    if dados['nome'] != '':
        break

while True:

    try:
        dados['partidas'] = int(input('\nNúmero de partidas: '))
        if 0 < dados['partidas'] < 6:
            break
    except ValueError:
        print('\nEntrada inválida.')
    
for c in range(1,dados['partidas']+1):

    while True:

        try:
            gol = int(input(f'\nGols na partida {c}: '))
            if gol > -1:
                gols.append(gol)
                break
        except ValueError:
            print('\nEntrada inválida.')

    if c == dados['partidas']:
        dados['gols'] = gols
        for gol in dados['gols']:
            total_de_gols += gol
        dados['total de gols'] = total_de_gols

print(), print(separador), print()
print(dados)
print(), print(separador),

for key, value in dados.items():

    print(f'\nO campo "{key}" tem o valor "{value}"')

print(), print(separador), print()

print(f'O jogador {dados["nome"]} jogou {dados["partidas"]} partidas:')

for a, gol in enumerate(dados['gols']):

    print(f'\n    Partida {a+1}: {gol} gols.')

print(f'\n  Total de gols: {dados["total de gols"]}')

print() 
for caractere in separador:
    print(caractere, end='', flush=True)
    sleep(0.03)
print('\n') 