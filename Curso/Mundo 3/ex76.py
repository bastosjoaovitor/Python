tupla = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.00, 'Canetas', 22.30, 'Livro', 34.90)

separador = f'{50*"-"}'

f = ''

print()
print(separador)
print(f'{"Lista de materias":^50}')
print(separador,'\n')

for c in range(0,18):
    if c % 2 == 0:
        f = f'{tupla[c]:<42}'
        f = f.replace(' ','.')
        print(f, end='R$')
    else:
        print(f'{tupla[c]:>6}')

print()