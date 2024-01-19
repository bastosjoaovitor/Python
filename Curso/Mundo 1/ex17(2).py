from math import hypot
print('\n{}\n'.format(20*'='))
co = float(input('Comprimento do cateto oposto: '))
print('')
ca = float(input('Comprimento do cateto adjacente: '))
print('\n{}\n'.format(20*'='))
print('A hipotenusa mede {:.2f}.'.format(hypot(co,ca)))
print('\n{}\n'.format(20*'='))