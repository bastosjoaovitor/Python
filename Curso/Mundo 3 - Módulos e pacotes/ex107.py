"""

from biblioteca import moeda

preco = float(input('\nDigite o preço: R$'))

print(f'''
A metade de R${preco} é R${moeda.metade(preco):.2f}
O dobro de R${preco} é R${moeda.dobro(preco):.2f}
Aumentando 10% fica R${moeda.aumentar(preco, 10):.2f}
Reduzindo 10% fica R${moeda.diminuir(preco, 10):.2f}
''')

"""