print(f'\n{25*"-="}-\n')
n1 = float(input('Digite o primeiro valor: '))
n2 = float(input('\nDigite o segundo valor: '))
n3 = float(input('\nDigite o terceiro valor: '))
print(f'\n{25*"-="}-\n')
n = n1, n2, n3
n = sorted(n)
print(f'O menor valor é o {n[0]}\n')
print(f'O maior valor é o {n[2]}')
print(f'\n{25*"-="}-\n')