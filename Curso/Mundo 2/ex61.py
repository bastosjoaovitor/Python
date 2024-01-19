verde = '\033[32m'
separador = f'{verde}\n{25*"-="}\n'
print(separador)
print('    Gerador de PA    ')
print(separador)
n1 = int(input('Primeiro termo: '))
n2 = int(input('\nRaxão da PA: '))
print()
for c in range(1,10):
    print(f'{n1} => ', end='')
    n1 += n2
print(f'{n1}\n')