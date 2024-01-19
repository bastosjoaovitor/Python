"""

from biblioteca import moeda

preco = float(input('\nDigite o preço: R$'))

print(f'''
A metade de {moeda.moeda(preco)} é {moeda.moeda(moeda.metade(preco))}
O dobro de {moeda.moeda(preco)} é {moeda.moeda(moeda.dobro(preco))}
Aumentando 10% fica {moeda.moeda(moeda.aumentar(preco, 10))}
Reduzindo 10% fica {moeda.moeda(moeda.diminuir(preco, 10))}
''')

"""