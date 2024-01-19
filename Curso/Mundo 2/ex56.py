class cores:
    azul = '\033[34m'
    ciano = '\033[36m'
    verde = '\033[32m'
    vermelho = '\033[31m'
    amarelo = '\033[33m'
    roxo = '\033[35m'
    fim = '\033[m'
separador = f'{cores.roxo}\n{25*"-="}\n{cores.fim}'
# cores

nomes = []
media = 0
idadehomens = []
mulheres_com_menos_de_20_anos = 0
# variveis

print(separador)

for c in range(1,5):
    print(f'{cores.verde}----{c}º PESSOA----')
    while True:
        try:
            nome = str(input(f'{cores.ciano}NOME: ')).strip().title()
            break
        except ValueError:
            print(f'{cores.vermelho}Entrada inválida.')
    while True:
        try:
            idade = int(input(f'{cores.ciano}Digite a idade: '))
            media += idade
            break
        except ValueError:
            print(f'{cores.vermelho}Entrada inválida.')
    while True:
        try:
            sexo = str(input(f'{cores.ciano}Sexo [M/F]: ')).upper().strip()
            if sexo == 'M':
                nomes += [nome]
                idadehomens += [idade]
                print()
                break
            elif sexo == 'F':
                if idade < 20:
                    mulheres_com_menos_de_20_anos += 1
                print()
                break
            else:
                print(f'{cores.vermelho}Entrada inválida.')
        except ValueError:
            print(f'{cores.vermelho}Entrada inválida.')
# coletando dados

if len(idadehomens) > 0:
    maior_numero = max(idadehomens)
    posicao = idadehomens.index(maior_numero)

print(f'{cores.verde}A média de idade do grupo é de {media/4:.0f} anos.\n')

if nomes == []:
    print('Não há homens no grupo.\n')
else:
    print(f'O homem mais velho do grupo é {nomes[posicao]} com {maior_numero} anos.\n')

if len(nomes) == 4:
    print('Não há mulheres no grupo.')
elif mulheres_com_menos_de_20_anos == 0:
    print('Das mulheres no grupo, nenhuma tem menos de 20 anos.')
elif mulheres_com_menos_de_20_anos == 4:
    print('Todas as mulheres do grupo tem menos de 20 anos.')
else:
    print(f'Das mulheres do grupo, {mulheres_com_menos_de_20_anos} tem menos de 20 anos.')
# respostas

print(separador)
# fim
