print(f'\n{10*"-="}-\n')
v = float(input('Digite a velocidade atual do carro: '))
print()
if v <= 80:
    print('Tenha um bom dia! Dirija com segurança!')
else:
    print(f'MULTADO! Você excedeu o limite permitido de 80km/h\nSua multa é de R${(v-80)*7}. ')
print(f'\n{20*"-="}-\n')