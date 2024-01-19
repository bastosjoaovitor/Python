a = 0
b = 0
c = 0
while True:
    n = int(input('\nDigite um número [0 para parar] : '))
    a += 1
    b += n
    if n == 0:
        a -= 1
        break
    elif a == 1:
        c = n
if a > 1:
    print(f'\nVocê digitou {a} números e a soma deles é igual a {b}.\n')
elif a == 1:
    print(f'\nVocê digitou apenas {c}.\n')
else:
    print('\nVocê não digitou nenhum número.\n')