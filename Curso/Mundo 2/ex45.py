
class cores:
    azul = "\033[34m"
    ciano = "\033[36m"
    verde = "\033[32m"
    amarelo = "\33[33m"
    vermelho = "\033[31m"
    fim = "\033[m"
separador = f'{cores.verde}\n{15*"-="}\n{cores.fim}'
# cores

print(separador)
print(f'\033[4;33m    PEDRA, PAPEL E TESOURA')
print(separador)
# texto inicial

print(f"""{cores.verde}[ {cores.amarelo}1{cores.verde} ]{cores.ciano} PEDRA
{cores.verde}[ {cores.amarelo}2{cores.verde} ]{cores.ciano} PAPEL
{cores.verde}[ {cores.amarelo}3{cores.verde} ]{cores.ciano} TESOURA""")
# opções

while True:
    try:
        escolha1 = int(input((f'{cores.ciano}\nSua jogada: {cores.amarelo}')))
        if escolha1 == 1 or escolha1 == 2 or escolha1 == 3:
            print()
            break
        else: 
            print(f'{cores.vermelho}\nEscolha pedra(1), papel(2) ou tesoura(3).')
    except ValueError:
        print(f'{cores.vermelho}\nEntrada inválida.')
# escolha

from random import randint
escolha2 = randint(1,3)
# escolha do computador
    
import time
print(f'{cores.verde}JO')
time.sleep(0.5)
print(f'{cores.verde}KEN')
time.sleep(0.5)
print(f'{cores.verde}PÔ\n')
# carregando

if escolha1 == 1:
    a = 'pedra'
elif escolha1 == 2:
    a = 'papel'
else:
    a = 'tesoura'

if escolha2 == 1:
    b = 'pedra'
elif escolha2 == 2:
    b = 'papel'
else:
    b = 'tesoura'

if escolha1 == escolha2:
    print(f'{cores.amarelo}EMPATE!\n\nVocê e eu escolhemos {a}.')
elif escolha1 == 1 and escolha2 == 2 or escolha1 == 2 and escolha2 == 3 or escolha1 == 3 and escolha2 == 1:
    print(f'{cores.vermelho}VOCÊ PERDEU!\n\nVocê escolheu {a} e eu escolhi {b},\nahahahaha, ruim, horrível, perdedor,\nhorroroso, muito ruim, achei fácil,\nizi, bot, desinstala, noob.')
else:
    print(f'{cores.verde}Você ganhou, eu escolhi {b} e você {a}.\nSorte de principiante, vai mais uma? ou vai correr?')
# resposta

print(separador)
# fim
