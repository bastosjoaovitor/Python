print(f'\n{25*"-="}-\n')
s = float(input('Digite o sálario do funcionário: R$'))
if s > 1250:
    print(f'\nO salário que antes era de R${s:.2f} agora com o aumento de 10% passa a ser de R${s + ((s/100)*10):.2f}')
else:
    print(f'\nO salário que antes era de R${s:.2f} agora com o aumento de 15% passa a ser de R${s + ((s/100)*15):.2f}')
print(f'\n{25*"-="}-\n')