class cores:
    azul = "\033[34m"
    amarelo = "\033[33m"
    vermelho = "\033[31m"
    ciano = "\033[36m"
    verde = "\033[32m"
    roxo = "\033[35m"
    fim = "\033[m"
# cores 

separador = f'{cores.vermelho}\n{20*"-= "}\n{cores.fim}'
# melhor legibilidade

print(separador)
print(f'\033[4;33m    LOJAS NÃO SEI O NOME{cores.fim}')
print(separador)
# texto inicial

while True:
    try:
        preco = float(input((f'{cores.ciano}  PREÇO DAS COMPRAS: {cores.verde}R$')))
        if preco > 0:
            break
        else:
            print(f'\n{cores.vermelho}Os produtos não são grátis.\n')
    except ValueError:
        print(f'\n{cores.vermelho}Entrada inválida.\n')
# preço

print(f'\033[4;33m\n  FORMAS DE PAGAMENTO{cores.fim}')
print(f'\n{cores.verde}    [ 1 ] à vista dinheiro/cheque(10% de desconto)')
print('    [ 2 ] à vista cartão(5% de desconto)')
print('    [ 3 ] 2x no cartão(preço normal)')
print('    [ 4 ] 3x até 12x no cartão(20% de juros)')
# formas de pagamento

while True:
    try:
        opcao = int(input(f'{cores.verde}\nDigite a opção: '))
        if opcao == 1 or opcao == 2 or opcao == 3 or opcao == 4:
            break
        else:
            print(f'\n{cores.vermelho}Entrada inválida.')
    except ValueError:
        print(f'\n{cores.vermelho}Entrada inválida.')
# opção de pagamento

if opcao == 4:
    while True:
        try:
            parcelas = int(input(f'\n{cores.ciano}Quantas parcelas: '))
            if 2 < parcelas < 13:
                break
            print(f'\n{cores.vermelho}Parcelas de 3x até 12x.')
        except ValueError:
            print(f'\n{cores.vermelho}Entrada inválida.')
# parcelas

if opcao == 1:
    print(f'\n{cores.amarelo}O total a pagar é de R${(preco/100)*90:.2f}')
elif opcao == 2:
    print(f'\n{cores.amarelo}O total a pagar é de R${(preco/100)*95:.2f}')
elif opcao == 3:
    print(f'\n{cores.amarelo}O total a pagar é de R${preco:.2f}, em 2x de R${preco/2:.2f}')
else:
    print(f'\n{cores.amarelo}O total a pagar é de R${preco*1.2:.2f}, em {parcelas}x de R${(preco*1.2)/parcelas:.2f}')
# preço final

print(separador)
# fim