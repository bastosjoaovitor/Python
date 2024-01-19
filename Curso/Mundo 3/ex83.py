expressao = input('\nDigite a expressão: ').upper().strip()

a = 0
b = 0
c = 0

for caractere in expressao:
    if caractere == '(':
        a += 1
    elif caractere == ')':
        b += 1
    if b > a:
        c += 1

if b != a:
    c += 1

if c != 0:
    print(f'\nA expressão é inválida.\n')
    exit()

a = 0
b = 0
c = 0

for caractere in expressao:
    if caractere == '[':
        a += 1
    elif caractere == ']':
        b += 1
    if b > a:
        c += 1

if b != a:
    c += 1

if c != 0:
    print(f'\nA expressão é inválida.\n')
    exit()

a = 0
b = 0
c = 0

for caractere in expressao:
    if caractere == '{':
        a += 1
    elif caractere == '}':
        b += 1
    if b > a:
        c += 1

if b != a:
    c += 1

if c == 0:
    print(f'\nA expressão é válida.\n')
else:
    print(f'\nA expressão é inválida.\n')