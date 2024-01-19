def fatorial(number, show=False):
    """
        
    => Calcula o fatorial de um número.
        :param number: O número a ser calculado
        :param show: (opcional) Mostrar ou não a conta
        :return: O fatorial de number
    """
    from random import randint
    soma = 1
    for n in range(number, 0, -1):
        soma *= n
        if show == True:
            print(n, end=' x ')
            if n == 1:
                print(f'\b\b= {soma}')
    if show == False:
        print(soma)
    return soma

print(40*"=")

while True:

    try:
        number = int(input('\nDigite um número para calcular seu fatorial: '))
        if number > 0:
            break
    except ValueError:
        print('\nEntrada inválida.')

while True:

    show = input('\nMostrar a conta? [S/N] : ').title()
    if show in ['S','N']:
        if show == 'S':
            show = True
        else:
            show = False
        break

print(), print(40*"-")
fatorial(number, show)
print(40*"-"), print()
print(40*"=")