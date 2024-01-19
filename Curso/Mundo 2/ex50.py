s = 0
a = 0
for c in range(1,7):
    n = int(input('Digite um número inteiro: '))
    if n % 2 == 0:
        s = s + n
        a = a + 1
print(f'Você informou {a} números pares e a soma foi {s}.')