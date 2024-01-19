from time import sleep
print('\nOs números de 1 a 500 ímpares e múltiplos de 3 são:\n')
s = 0
for c in range(1,500):
    if c % 2 == 1 and c % 3 == 0:
        s = s + c
        print(c)
        sleep(0.05)
print(f'\nA soma desses números é igual a {s}')
print('\nCABO\n')