from math import hypot
print('')
print(20*'=')
print('')
co = float(input('Comprimento do cateto oposto: '))
print('')
ca = float(input('Comprimento do cateto adjacente: '))
h = hypot(co,ca)
print('')
print(20*'=')
print('')
print('A hipotenusa mede {:.2f}.'.format(h))
print('')
print(20*'=')
print('')