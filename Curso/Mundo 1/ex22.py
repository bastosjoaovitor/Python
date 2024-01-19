print(f'\n{20*"="}\n')
n = input('Digite seu nome completo: ').strip()
print(f'\n{20*"="}\n')
d = n.split()
print('Analisando seu nome...\n')
print(f"""Seu nome em maiúsculas é {n.upper()}.
Seu nome em minúsculas é {n.lower()}.
Seu nome ao todo tem {len(n) - n.count(' ')} letras.
Seu primeiro nome é {d[0]} e tem {len(d[0])} letras.""")
print(f'\n{20*"="}\n')