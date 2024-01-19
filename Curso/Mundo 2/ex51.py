print(27*'=')
print('    10 TERMOS DE UMA PA     ')
print(27*'=','\n')
n = int(input('Digite o primeiro valor: '))
r = int(input('\nDigite a razão: '))
print()
print(f'{n} ', end='')
for c in range(1,10):
    n = n + r
    print(f'-> {n} ', end='')
print('\n\nCABO\n')
print(27*'=')