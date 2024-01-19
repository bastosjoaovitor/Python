print(f'\n\033[36m{25*"-="}-\033[m\n')
print(f'\033[4mEmpréstimo bancário\033[m')
print(f'\n\033[36m{25*"-="}-\033[m\n')
valor_da_casa = float(input('Qual é o valor da casa? R$')) 
salario = float(input('\nQual é o seu salário? R$'))
tempo = int(input('\nEm quantos anos deseja pagar? ')) * 12
prestacao_mensal = valor_da_casa / tempo
print(f'\n\033[36m{25*"-="}-\033[m\n')
if prestacao_mensal <= (salario / 100) * 30:
    print(f'\033[4mSeu empréstimo de R${valor_da_casa:.2f} foi aprovado, a prestação mensal a pagar é de R${prestacao_mensal:.2f}\033[m')
else:
    print(f'\033[4mSeu empréstimo foi negado, a prestação mensal seria de R${prestacao_mensal:.2f}, o que ultrapassa o limite de 30% do seu salário.\033[m')
print(f'\n\033[36m{25*"-="}-\033[m\n')