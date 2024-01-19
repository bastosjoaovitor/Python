ano1 = int(input('\nDigite o ano em que a primeira pessoa nasceu: '))
ano2 = int(input('\nDigite o ano em que a segunda pessoa nasceu: '))
ano3 = int(input('\nDigite o ano em que a terceira pessoa nasceu: '))
ano4 = int(input('\nDigite o ano em que a quarta pessoa nasceu: '))
ano5 = int(input('\nDigite o ano em que a quinta pessoa nasceu: '))
ano6 = int(input('\nDigite o ano em que a sexta pessoa nasceu: '))
ano7 = int(input('\nDigite o ano em que a sétima pessoa nasceu: '))

import datetime
data_atual = datetime.date.today().year

datas = [ano1, ano2, ano3, ano4, ano5, ano6, ano7]

maiores_de_idade = 0
menores_de_idade = 0

for c in range(0,7):
    if datas[c] <= 2005:
        maiores_de_idade += 1
    else:
        menores_de_idade += 1

if maiores_de_idade == 7:
    print('\nTodos são maiores de idade.\n')
elif menores_de_idade == 7:
    print('\nTodos são menores de idade.\n')
else:
    print(f'\nDessas 7 pessoas, {maiores_de_idade} são maiores de idade e {menores_de_idade} são menores de idade.\n')
