class cores:
    vermelho = '\033[31m'
    ciano = '\033[36m'
    amarelo = '\033[33m'
    verde = '\033[32m'
    azul = '\033[34m'
    fim = '\033[m'
separador = f'{cores.azul}\n{25*"="}\n{cores.fim}'
# Cores e separaçoes

a = 2
b = 0
# Variaveis

print(separador)
print(f'\033[33;4m    Progressão Aritmética    {cores.fim}')
print(separador)
# Título

while True:

    if a == 1:

        while True:
            try:
                b = int(input(f'Quantos termos você quer que mostre a mais: '))
                if b < 1:
                    print(f'{cores.vermelho}\nEscolha no mínimo 1 termo pra mostrar a mais.\n{cores.fim}')
                else:
                    print()
                    break
            except ValueError:
                print(f'{cores.vermelho}\nEntrada inválida.\n{cores.fim}')

        for i in range(1,b+1):
            print(f'{cores.verde}{termo1} => ', end='')
            termo1 += razao
        print(f'{termo1}{cores.fim}\n')
        # Saber termos a mais

    elif a == 2:

        while True:
            try:
                termo1 = float(input('Digite o primeiro termo: '))
                break
            except ValueError:
                print(f'{cores.vermelho}\nEntrada inválida.\n{cores.fim}')

        while True:
            try:
                razao = float(input('\nDigite a razão: '))
                print()
                break
            except ValueError:
                print(f'{cores.vermelho}\nEntrada inválida.{cores.fim}')

        for i in range(1,10):
            print(f'{cores.verde}{termo1} => ', end='')
            termo1 += razao
        print(f'{termo1}{cores.fim}\n')
        # Nova PA
    
    elif a == 3:

        while True:
            try:
                confirmacao = input('Confirma? [S/N] : ').strip().upper()
                confirmacao = confirmacao[0]
                if confirmacao in ['S','N']:
                    print()
                    break
                else:
                    print(f'{cores.vermelho}\nDigite "S" ou "N".\n{cores.fim}')
            except ValueError:
                print(f'{cores.vermelho}\nEntrada inválida.\n{cores.fim}')

        if confirmacao == 'S':
            print(f'Programa finalizado.')
            print()
            break
        # Finalizar programa

    print(f'''{cores.fim}opções:\n
[ 1 ] - Saber mais termos dessa PA
[ 2 ] - Criar uma nova PA
[ 3 ] - Finalizar programa\n''')
    
    while True:
        try:
            a = int(input('Escolha: '))
            if a in [1,2,3]:
                print()
                break
            else:
                print(f'{cores.vermelho}\nDigite uma das opções disponíveis.\n{cores.fim}')
        except ValueError:
            print(f'{cores.vermelho}\nEntrada inválida.\n{cores.fim}')

# fim