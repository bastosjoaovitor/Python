separador = f'\033[34m\n{25*"-="}\n\033[m'
# separador das frases para melhor compreensão

amarelo = "\033[33m"
azul = "\033[36m"
vermelho = "\033[31m"
fim =  "\033[m"
# cores

print(separador)
print(f'{amarelo}Verifique se foi aprovado{fim}')
print(separador)
# texto inicial

while True:
    try:
        N1 = float(input(f'Quanto você tirou(prova valendo 10): {amarelo}'))
        if 0 <= N1 <= 10:
            break
        else:
            print(f'{vermelho}\nEntrada inválida.\n{fim}')
    except ValueError:
        print(f'{vermelho}\nEntrada inválida.\n{fim}')

while True:
    try:
        N2 = float(input(f'{fim}\nQuanto você tirou(trabalho valendo 8): {amarelo}'))
        if 0 <= N2 <= 8:
            break
        else:
            print(f'{vermelho}\nEntrada inválida.\n{fim}')
    except ValueError:
        print(f'{vermelho}\nEntrada inválida.\n{fim}')

while True:
    try:
        N3 = float(input(f'{fim}\nQuanto você tirou(caderno valendo 7): {amarelo}'))
        if 0 <= N3 <= 7:
            break
        else:
            print(f'{vermelho}\nEntrada inválida.\n{fim}')
    except ValueError:
        print(f'{vermelho}\nEntrada inválida.\n{fim}')

nota_final = N1 + N2 + N3
# notas

print(separador)

if nota_final == 25:
    print(f'{amarelo}Você tirou a nota máxima!!!Parabéns, continue assim.')
elif nota_final >= 15 < 25:
    print(f'{azul}Você foi aprovado.')
elif nota_final >= 5 < 15:
    print(f'{vermelho}Reprovado.')
else:
    print(f'{vermelho}Um cachorro no seu lugar tiraria uma nota mais alta, decepcionante.')
#resultados

print(separador)
#fim
