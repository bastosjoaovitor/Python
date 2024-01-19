azul = "\033[34m"
amarelo = "\033[33m"
vermelho = "\033[31m"
ciano = "\033[36m"
fim = "\033[m"
# cores

separador = f'{azul}\n{25*"-="}\n{fim}'
# separador das frases para melhor compreensão

print(separador)
print('\033[4;33mVEJA A CATEGORIA DO ATLETA\033[m')
print(separador)
# texto inicial

while True:
    try:
        idade = int(input(f'{ciano}Para saber a categoria do atleta, digite sua idade(somente números): {amarelo}'))
        break
    except ValueError:
        print(f'{vermelho}\nEntrada inválida.\n{fim}')
# idade 

if idade <= 0:
    print(f'{ciano}\nCategoria do atleta: {vermelho}INEXISTENTE.')
elif 0 < idade <= 9:
    print(f'{ciano}\nCategoria do atleta: {amarelo}MIRIM.')
elif 9 < idade <= 14:
    print(f'{ciano}\nCategoria do atleta: {amarelo}INFANTIL.')
elif 14 < idade <= 19:
    print(f'{ciano}\nCategoria do atleta: {amarelo}JÚNIOR.')
elif 19 < idade <= 25:
    print(f'{ciano}\nCategoria do atleta: {amarelo}SÊNIOR.')
elif 25 < idade < 100:
    print(f'{ciano}\nCategoria do atleta: {amarelo}MASTER.')
else:
    print(f'{ciano}\nCategoria do atleta: {vermelho}MORTO.')
# resposta

print(separador)