dados = []
continuar = 'S'
total_cadastros = 0
media_idade = 0
a = 0
mulheres_cadastradas = []
pessoas_com_idade_acima_da_media = []
separador = f'{40*"="}'

from time import sleep

print(), print(separador), print(f'{"\033[4mCADASTRO\033[m":^45}'), print(separador)

while continuar == 'S':

    total_cadastros += 1

    pessoa = {}

    while True:

        pessoa['nome'] = input('\nNome: ').strip().title()
        if pessoa['nome'] != '':
            break
        else:
            print('\nEntrada inválida.')

    while True:

        try:
            pessoa['idade'] = int(input('\nIdade: '))
            if pessoa['idade'] > 0:
                break
            else:
                print('\nEntrada inválida.')
        except ValueError:
            print('\nEntrada inválida.')

    while True:

        pessoa['sexo'] = input('\nSexo [M/F] : ').upper()
        if pessoa['sexo'] in ['M','F']:
            break
        else:
            print('\nDigite "M" ou "F".')
    
    while True:

        continuar = input('\nAdicionar outra pessoa [S/N]: ').upper()
        if continuar in ['S','N']:
            break
        else:
            print('\nDigite "S" ou "N".')

    dados.append(pessoa)

    if continuar == 'N':

        for i, pessoa in enumerate(dados):
            media_idade += dados[i]['idade']
            a += 1
        media_idade = media_idade / a

        for pessoa in dados:
            
            if pessoa['sexo'] == 'F':
                mulheres_cadastradas.append(pessoa['nome'])
                print(pessoa['nome'])

print(), print(separador), print()

print(f'''Total de pessoas cadastradas: {total_cadastros}
Média de idade: {media_idade:.0f}
Mulheres cadastradas: {mulheres_cadastradas}
Pessoas com idade acima da média:''')

for pessoa in dados:
            
    if pessoa['idade'] > media_idade:

        print(f' -> {pessoa['nome']} com {pessoa['idade']} anos.')

for letra in f'\nFinalizando programa''...\n\nAdeus\n':
    if letra == ".":
        sleep(0.5)
        print(letra, end='', flush=True)
        sleep(0.5)
    else:
        print(letra, end='', flush=True)
        sleep(0.05)

print(), print(separador), print()