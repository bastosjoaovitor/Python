print('')
print(20*'=')
print('')
s = float(input('Digite o valor do salário do funcionário: '))
print('')
a = float(input('Digite a porcentagem do aumento do funcionário: '))
print('')
print(20*'=')
print('')
print('O salário do funcionário que antes era de R${:.2f}, com {:.2f}% de aumento, passa a ser de R${:.2f}'.format(s,a,s*(100+a)/100))
print('')
print(20*'=')
print('')