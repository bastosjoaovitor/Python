class cores:
    verde = "\033[32m"
    vermelho = "\033[31m"
    fim = "\033[m"
print()
while True:
    try:
        n1 = int(input('Digite um número: '))
        break
    except ValueError:
        print(f'{cores.vermelho}\nEntrada inválida.{cores.fim}\n')
print()
print(f'O número {n1} é divisivel pelos números em verde.\n')
print(f'{cores.verde}1 ', end='')
s = 0
for c in range(2,n1):
    if n1 % c == 0:
        print(f'{cores.verde}{c} ',end='')
        s = s + 1
    elif n1 % c != 0:
        print(f'{cores.vermelho}{c} ',end='')
print(f'{cores.verde}{n1}\n')
if s == 0:
    print(f'{cores.verde}O número {n1} é PRIMO, pois é divisível somente por 1 e por ele mesmo.{cores.fim}')
else:
    print(f'{cores.vermelho}O número {n1} NÃO É PRIMO, pois não é divisível somente por 1 e por ele mesmo.{cores.fim}')
print()