def leiaint(msg):
    '''
    => Faz um input e valida somente se for um valor númerico.
    :param msg: A mensagem que aparece no input
    '''
    while True:

        try:
            valor = int(input(msg))
            break
        except ValueError:
            print('\n\033[31mEntrada inválida.\033[m')
    return valor

number = leiaint('\nDigite um número inteiro: ')

print(f'\nVocê digitou o número {number}.\n')