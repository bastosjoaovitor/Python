print(f'\n{25*"=-"}=')
print(f'{"CADASTRE UMA PESSOA":^50}')
print(f'{25*"=-"}=')

c = 'S'
pessoas_com_mais_de_18_anos = 0
homens_cadastrados = 0
mulheres_com_menos_de_20_anos = 0

while c == 'S':

    idade = int(input('\nDigite a idade da pessoa: '))
    sexo = str(input('\nDigite o sexo, (M) para masculino ou (F) para feminino: ')).upper()

    if idade > 18:
        pessoas_com_mais_de_18_anos += 1

    if sexo == 'M':
        homens_cadastrados += 1
    
    elif sexo == 'F':
        if idade < 20:
            mulheres_com_menos_de_20_anos += 1

    c = input('\nDeseja cadastrar mais alguém [S/N]: ').upper()

    if c != 'S':
        break

print(f'\nDas pessoas que você cadastrou {pessoas_com_mais_de_18_anos} tem mais de 18 anos, {homens_cadastrados} são homens e {mulheres_com_menos_de_20_anos} são mulheres com menos de 20 anos.\n\nPrograma finalizado.\n')