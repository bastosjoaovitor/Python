print(f'\033[34m\n{25*"-="}\n\033[m')
while True:
    try:
        N = int(input('\033[36mDigite um número inteiro para convertê-lo: \033[33m'))
        break
    except ValueError:
        print('\033[31m\nEntrada inválida.\n\033[m')
print("""\033[36m\nEscolha uma das opções para conversão:
[ \033[32m1\033[m \033[36m] converter para BINÁRIO
[ \033[32m2\033[m \033[36m] converter para OCTAL
[ \033[32m3\033[m \033[36m] converter para HEXADECIMAL\n""")
while True:
    try:
        opcao = int(input('\033[36mSua opção: \033[32m'))
        if opcao == 1 or opcao == 2 or opcao == 3:
            break
        else:
            print('\033[31m\nEntrada inválida.\n\033[m')
    except ValueError:
        print('\033[31m\nEntrada inválida.\n\033[m')
if opcao == 1:
    print(f'\033[36m\nO número \033[33m{N}\033[m \033[36mconvertido em BINÁRIO vira \033[33m{bin(N)[2::]}\033[m')
elif opcao == 2:
    print(f'\033[36m\nO número \033[33m{N}\033[m \033[36mconvertido em OCTAL vira \033[33m{oct(N)[2::]}\033[m')
elif opcao == 3:
    print(f'\033[36m\nO número \033[33m{N}\033[m \033[36mconvertido em HEXADECIMAL vira \033[33m{hex(N)[2::]}\033[m')
print(f'\033[34m\n{25*"-="}\n\033[m')