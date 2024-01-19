from random import choice
print(f'\n{20*"="}\n')
a = input('Primeiro aluno: ')
b = input('\nSegundo aluno: ')
c = input('\nTerceiro aluno: ')
d = input('\nQuarto aluno: ')
print(f'\n{20*"="}\n\nO aluno sorteado foi {choice([a,b,c,d])}.\n\n{20*"="}\n')