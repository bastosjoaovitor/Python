from datetime import date
separador = f'\033[34m\n{25*"-="}\n\033[m'

print(separador)
print('\033[4;32mALISTAMENTO MILITAR\033[m')
print(separador)

while True:
    try:
        data_de_nascimento = int(input('\033[32mDigite o ano que você nasceu: \033[33m'))
        break
    except ValueError:
        print('\033[31m\nEntrada inválida.\n')

idade = date.today().year - data_de_nascimento

if idade == 18:
    print('\033[32mVá se alistar IMEDIATAMENTE!')
elif idade < 18:
    print(f'\033[32mVocê ainda não tem idade para se alistar, você deverá se alistar em {data_de_nascimento+18}.')
else:
    print(f'\033[32mVocê já deveria ter se alistado há {idade - 18} anos.')
    print(f'Seu alistamento foi em {data_de_nascimento + (idade-(idade - 18))}.')

print(separador)