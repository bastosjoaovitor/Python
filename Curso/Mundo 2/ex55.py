maiorpeso = 0
menorpeso = 10000000000000000000000000

for c in range(1,6):
    peso = float(input(f'\nPeso da {c}º pessoa: '))
    if peso > maiorpeso:
        maiorpeso = peso
    elif peso < menorpeso:
        menorpeso = peso

print(f'\nO maior peso registrado foi de {maiorpeso}kg e o menor foi de {menorpeso}kg.')
    