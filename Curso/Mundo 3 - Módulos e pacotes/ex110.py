from biblioteca.moeda import resumo

preco = float(input('\nDigite o preço: '))
aumento = float(input('\nDigite o aumento: '))
desconto = float(input('\nDigite o desconto: '))

print(f'\n{30*"-"}')
print(F'{"\033[4mRESUMO DO VALOR\033[m":^30}')
print(f'{30*"-"}\n')
resumo(preco, aumento, desconto)
print(f'\n{30*"-"}')
