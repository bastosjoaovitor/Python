from time import sleep
from datetime import datetime

dados = {}

print(f'\n{40*"="}')

while True:
        
    nome = input('\nNome: ')
    if nome != '':
        dados['nome'] = nome
        break

while True:

    try:

        ano_de_nascimento = int(input('\nAno de nascimento: '))
        if ano_de_nascimento > 0:
            dados['ano de nascimento'] = ano_de_nascimento
            break
    except ValueError:
        print('\nEntrada inválida.')

while True:

    try:

        carteira_de_trabalho = int(input('\nCarteira de trabalho (0 não tem) : '))
        if carteira_de_trabalho >= 0:
            dados['ctps'] = carteira_de_trabalho
            break
    except ValueError:
        print('\nEntrada inválida.')

if carteira_de_trabalho > 0:

    while True:

        try:

            dados['ano de contratação'] = int(input('\nAno de contratação: '))
            if dados['ano de contratação'] > -1:
                break
        except ValueError:
            print('\nEntrada inválida.')

    while True:

        try:

            dados['salario'] = float(input('\nSalário: R$'))
            if dados['salario'] > 0:
                break
        except ValueError:
            print('\nEntrada inválida.')

dados['idade'] = datetime.now().year - dados['ano de nascimento']

if dados['ctps'] > 0:
    dados['idade de aposentadoria'] = dados['idade'] + (35 - (datetime.now().year - dados['ano de contratação']))

print(f'\n{40*"="}')

print(f'''
- Nome: {dados["nome"]}
- Idade: {dados["idade"]} anos
- Ctps: {dados["ctps"]}''')

if dados['ctps'] > 0:
    print(f'''- Ano de contratação: {dados["ano de contratação"]}
- Salário: R${dados["salario"]:.2f}
- Aposenta com {dados["idade de aposentadoria"]} anos''')
    
print()
    
for caractere in f"{40*'='}":
    print(caractere, end='', flush=True)
    sleep(0.03)

print()