a = 0
valor = 0
lista = []
from time import sleep

while a != 5:
    try:
        if a == 0:
            valor = int(input('\nDigite um número: '))
            lista.append(valor)
        else:
            valor = int(input('\nMais um: '))
            inserido = False
            for i, elemento in enumerate(lista):
                if valor < elemento:
                    lista.insert(i, valor)
                    inserido = True
                    break
            if not inserido:
                lista.append(valor)
        a += 1

    except ValueError:
        print('\nEntrada inválida.')

print()

mensagem = f'Esses são os valores que você digitou em ordem: {lista}'
fim = 'Finalizando...'

for m in mensagem:
    print(m, end='', flush = True)
    sleep(0.03)

print('\n')

for f in fim:
    print(f, end='', flush = True)
    sleep(0.05)

print('\n')
