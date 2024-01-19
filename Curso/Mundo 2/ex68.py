# 0 é par
# 1 é ímpar
from random import randint
v = 0
while True:
    print(f'\n{20*"=-"}\n           Jogo Par ou ímpar\n{20*"=-"}\n')
    e = input('Digite (P) para Par ou (I) para Ímpar: ').upper()
    n = int(input('\nDigite um número : '))
    z = randint(1,10)
    if e == 'P':
        if (n + z) % 2 == 0:
            print(f'\nVocê Jogou {n} e o computador jogou {z}, PAR!\nVocê ganhou! Revanche!!!')
            v += 1
        else:
            print(f'\nVocê Jogou {n} e o computador jogou {z}, ÍMPAR!\nAté agora você ganhou {v} vezes, parabéns!\nMas você perdeu! O jogo acabou!!!\n')
            break
    if e == 'I':
        if (n + z) % 2 == 1:
            print(f'\nVocê Jogou {n} e o computador jogou {z}, ÍMPAR!\nVocê ganhou! Revanche!!!')
            v += 1
        else:
            print(f'\nVocê Jogou {n} e o computador jogou {z}, PAR!\nAté agora você ganhou {v} vezes, parabéns!\nMas você perdeu! O jogo acabou!!!\n')
            break