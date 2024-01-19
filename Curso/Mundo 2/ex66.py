s = 0
soma = 0

while True:
    n = int(input('\nDigite um número: '))
    s += 1
    if n == 999:
        break
    soma += n

print(f'\nVocê digitou {s} números e a soma deles é igual a {soma}\n')