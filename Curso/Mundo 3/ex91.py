from random import randint
from operator import itemgetter
from time import sleep

dados = {
        'João':    randint(1,20),
        'Gustavo': randint(1,20),
        'Pedro':   randint(1,20),
        'Kaua':    randint(1,20),
        }

ranking = sorted(dados.items(), key=itemgetter(1), reverse=True)

for i, v in enumerate(ranking):

    print(f'\n{i+1}º lugar: {v[0]} com {v[1]} pontos.')
    sleep(0.5)

print()