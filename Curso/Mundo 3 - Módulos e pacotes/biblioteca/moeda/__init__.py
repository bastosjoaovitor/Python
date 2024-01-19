def aumentar(number, aumento, formatar = False, moeda = 'R$'):
    number += (number/100)*aumento
    if formatar == True:
        number = "{:.2f}".format(number)
        number = f'R${str(number)}'
        number = number.replace('.', ',')
    return number

def diminuir(number, desconto, formatar = False, moeda = 'R$'):
    number -= (number/100)*desconto
    if formatar == True:
        number = "{:.2f}".format(number)
        number = f'R${str(number)}'
        number = number.replace('.', ',')
    return number

def dobro(number, formatar = False, moeda = 'R$'):
    number *= 2
    if formatar == True:
        number = "{:.2f}".format(number)
        number = f'R${str(number)}'
        number = number.replace('.', ',')
    return number

def metade(number, formatar = False, moeda = 'R$'):
    number /= 2
    if formatar == True:
        number = "{:.2f}".format(number)
        number = f'R${str(number)}'
        number = number.replace('.', ',')
    return number

def moeda(number, moeda = 'R$'):
    number = "{:.2f}".format(number)
    number = f'{moeda}{str(number)}'
    number = number.replace('.', ',')
    return number

def resumo(number, aumento = 0, desconto = 0):
    print(f'''{'Preço analisado:':<20}{moeda(number)}
{'Dobro do preço:':<20}{moeda(dobro(number))}
{'Metade do preço:':<20}{moeda(metade(number))}
{f'{aumento}% de aumento:':<20}{moeda(aumentar(number, aumento))}
{f'{desconto}% de desconto:':<20}{moeda(diminuir(number, desconto))}''')
    
def leiadinheiro():
    while True:
        number = input('\nDigite o preço: R$').strip()
        number = number.replace(',','.')
        try:
            number = float(number)
        except ValueError:
            print(f'\n\033[31mERRO: "{number}" é um preço inválido.\033[m')
            continue
        print(f'\n{30*"-"}')
        print(F'{"\033[4mRESUMO DO VALOR\033[m":^30}')
        print(f'{30*"-"}\n')
        resumo(number, 10, 10)
        print(f'\n{30*"-"}')
        print()
        break
    return number