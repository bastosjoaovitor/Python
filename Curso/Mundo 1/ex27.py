print(f'\n{20*"="}\n')
nome = input('Digite seu nome: ').strip().split()
a = len(nome)
print(f'Seu primeiro nome é {nome[0]} e seu último nome é {nome[a-1]}.')