from random import choices
print(f'\n{20*"="}\n')
a = input('Primeiro aluno: ')
b = input('\nSegundo aluno: ')
c = input('\nTerceiro aluno: ')
d = input('\nQuarto aluno: ')
e = input('\nQuinto aluno: ')
print(f'\n{20*"="}\n\nA ordem de apresentação do trabalho será {choices([a,b,c,d,e], k=5)}.\n\n{20*"="}\n')