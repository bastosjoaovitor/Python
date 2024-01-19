from biblioteca import moeda

preco = float(input('\nDigite o preço: R$'))

print(f'''
A metade de {moeda.moeda(preco)} é {moeda.metade(preco, True)}
O dobro de {moeda.moeda(preco)} é {moeda.dobro(preco, True)}
Aumentando 10% fica {moeda.aumentar(preco, 10, True)}
Reduzindo 10% fica {moeda.diminuir(preco, 10, True)}
''')