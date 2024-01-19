print(f'\n{20*"="}')
n1 = float(input('\nDigite a primeira nota do aluno: '))
n2 = float(input('\nDigite a segunda nota do aluno: '))
n3 = float(input('\nDigite a terceira nota do aluno: '))
print(f'\n{20*"="}\n')
m = (n1 + n2 + n3) / 3
if 9 <= m <= 10:
    print(f'Sua média foi {m:.1f}!!!Parabéns!!!')
if 6 <= m < 9:
    print(f'Sua média foi {m:.1f}!Boa.')
if 3 <= m < 6:
    print(f'Sua média foi {m:.1f}. estude mais.')
if 0 <= m < 3:
    print(f'Sua média foi {m:.1f}, péssimo, estude mais.')
print(f'\n{20*"="}\n')