print(f'\n{25*"-="}-\n')
km = float(input('Quantos km foram percorridos: '))
print()
if km <= 200:
    print(f'O valor a pagar é de R${km*0.5:.2f}')
else:
    print(f'O valor a pagar é de R${km*0.45:.2f}')
print(f'\n{25*"-="}-\n')