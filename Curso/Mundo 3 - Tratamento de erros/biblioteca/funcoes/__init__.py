def leiaint():
    '''
    => Faz um input e valida somente se for um valor inteiro.
    '''
    while True:
        try:
            valor = input('\nDigite um número inteiro: ').strip()
            if valor == '':
                valor = 0
            valor = int(valor)
            break
        except ValueError:
            print(f'\n\033[31m"{valor}" é uma entrada inválida, por favor, digite um número inteiro.\033[m')
        except KeyboardInterrupt:
            print('\n\n\033[31mPrograma interrompido.\033[m')
    return valor

def leiareal():
    '''
    => Faz um input e valida somente se for um valor real.
    '''
    while True:
        try:
            real = input('\nDigite um número real: ').strip()
            real = real.replace(',', '.')
            if real == '':
                real = 0
            real = float(real)
            break
        except ValueError:
            print(f'\n\033[31m"{real}" é uma entrada inválida, por favor, digite um número real.\033[m')
        except KeyboardInterrupt:
            print('\n\n\033[31mPrograma interrompido.\033[m')
    return real