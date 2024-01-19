from random import randint
print(f'\n{20*"="}\n')
N = randint(1,5)
N2 = int(input(f'O computador pensou em um número de 1 a 5, em qual número você acha que ele pensou? '))
print('')
if N2 == N:
    print('Acertou!')
else:
    print('Errrooooooooooooouu!!!')
print(f'\n{20*"="}\n')