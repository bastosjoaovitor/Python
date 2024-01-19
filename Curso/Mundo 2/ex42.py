azul = "\033[34m"
amarelo = "\033[33m"
ciano = "\033[36m"
vermelho = "\033[31m"
fim = "\033[m"
# cores

separador = f'{azul}\n{20*"-="}\n{fim}'
# separador das frases para melhor compreensão

print(separador); print(f'\033[4;33mAnalisador de triângulos{fim}'); print(separador)
# texto inicial

print(f'{ciano}Digite 3 segmentos abaixo para saber se\né possível formar um triângulo com eles,\ne se for, qual tipo de triângulo é formado.\n{fim}')

while True:
    try:
        segmento_1 = float(input(f'{ciano}Primeiro segmento: {amarelo}'))
        break
    except ValueError:
        print(f'{vermelho}\nEntrada inválida.{fim}\n')

while True:
    try:
        segmento_2 = float(input(f'{ciano}\nSegundo segmento: {amarelo}'))
        break
    except ValueError:
        print(f'{vermelho}\nEntrada inválida.{fim}')

while True:
    try:
        segmento_3 = float(input(f'{ciano}\nTerceiro segmento: {amarelo}'))
        break
    except ValueError:
        print(f'{vermelho}\nEntrada inválida.{fim}')
# segmentos

print(separador)

if segmento_1 + segmento_2 > segmento_3 and segmento_2 + segmento_3 > segmento_1 and segmento_3 + segmento_1 > segmento_2:
    if segmento_1 == segmento_2 == segmento_3:
        print(f'{ciano}Os segmentos {amarelo}{segmento_1}{ciano}, {amarelo}{segmento_2}{ciano}, e {amarelo}{segmento_3}{ciano} formam um triângulo {amarelo}equilátero.')
    elif segmento_1 == segmento_2 or segmento_2 == segmento_3 or segmento_3 == segmento_1:
        print(f'{ciano}Os segmentos {amarelo}{segmento_1}{ciano}, {amarelo}{segmento_2}{ciano}, e {amarelo}{segmento_3}{ciano} formam um triângulo {amarelo}isósceles.')
    else:
        print(f'{ciano}Os segmentos {amarelo}{segmento_1}{ciano}, {amarelo}{segmento_2}{ciano}, e {amarelo}{segmento_3}{ciano} formam um triângulo {amarelo}escaleno.')
else:
    print(f'{vermelho}Os segmentos {amarelo}{segmento_1}{vermelho}, {amarelo}{segmento_2}{vermelho}, e {amarelo}{segmento_3}{vermelho} não podem formar um triângulo.')
# resposta

print(separador)
# fim
