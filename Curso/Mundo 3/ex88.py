lista = []

from sys import exit
from random import randint
from time import sleep

print(f'\n{40*"="}')
print(f'{"\033[4mGerador de jogos da Mega sena\033[m":^47}')
print(f'{40*"="}\n')


while True:

    try:
        jogos = int(input('\nQuantos jogos você quer que eu sorteie: '))
        if jogos < 0:
            print(f'\nNão da pra sortear {jogos} jogos.\nPrograma finalizado.\n')
            exit()
        elif jogos == 0:
            print('\nVocê escolheu não sortear um jogo, programa finalizado.\n')
            exit()
        elif jogos > 100:
            print('\nAi ce ta querendo demais, programa finalizado.\n')
            exit()
        else:
            break
    except ValueError:
        print('\nEntrada inválida.')

print('\nEsses são os jogos sorteados: ')

for valores in range(0,jogos):
    
    for sorteio in range(0,6):

        if sorteio == 0:
            numeros_ja_sorteados = []
        while True:
            numero = randint(1,60)
            if numero not in numeros_ja_sorteados:
                numeros_ja_sorteados.append(numero)
                numeros_ja_sorteados.sort()
                break
            else:
                continue
        if sorteio == 5:
            lista.append(numeros_ja_sorteados[:])

    print(f'\nJogo {valores+1} => {lista[valores]}')
    sleep(0.1)

print('\nPrograma finalizado.')