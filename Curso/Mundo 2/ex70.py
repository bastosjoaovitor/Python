print(f'\n{25*"=-"}=')
print(f'{"LOJA PYTHON":^50}')
print(f'{25*"=-"}=')

c = 'S'
total_gasto = 0
quantidade_de_produtos_que_custam_mais_de_1000_reais = 0
produto_mais_barato = ''
preço_do_produto_mais_barato = 0

while c == 'S':

    while True:
        try:
            nome_do_produto = input('\nDigite o nome do produto: ').strip()
            if nome_do_produto != '':
                break
            else:
                print('\nEntrada inválida.')
        except ValueError:
            print('\nEntrada inválida.')
        
    while True:
        try:
            preço_do_produto = float(input('\nDigite o preço do produto: R$'))
            if preço_do_produto > 0.00:
                break
        except ValueError:
            print('\nEntrada inválida.')

    if total_gasto == 0:
        produto_mais_barato = nome_do_produto
        preço_do_produto_mais_barato = preço_do_produto
    elif total_gasto != 0:
        if preço_do_produto < preço_do_produto_mais_barato:
            produto_mais_barato = nome_do_produto
            preço_do_produto_mais_barato = preço_do_produto

    total_gasto += preço_do_produto

    if preço_do_produto > 1000:
        quantidade_de_produtos_que_custam_mais_de_1000_reais += 1

    while True:
        try:
            c = input('\nVocê deseja adicionar mais algum produto [S/N]: ').upper().strip()
            if c != '':
                c = c[0]
                if c == 'S' or c == 'N':
                    break
                else:
                    print('\nEntrada inválida.')
            else:
                print('\nEntrada inválida.')
        except ValueError:
            print('\nEntrada inválida.')

print(f'\n{25*"=-"}=\n\nTotal a pagar: R${total_gasto:.2f}\n\n{quantidade_de_produtos_que_custam_mais_de_1000_reais} produtos custam mais de R$1000\n\nProduto mais barato: {produto_mais_barato} R${preço_do_produto_mais_barato:.2f}\n\n{25*"=-"}=\n\nPrograma finalizado.\n')