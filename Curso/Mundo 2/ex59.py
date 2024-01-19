class cores:
    vermelho = '\033[31m'
    ciano = '\033[36m'
    amarelo = '\033[33m'
    verde = '\033[32m'
    azul = '\033[34m'
    fim = '\033[m'
separador = f'{cores.azul}\n{25*"="}\n{cores.fim}'
# cores e separaçoes

print(separador)
print(f'\033[33;4mDigite dois valores para saber somá-los, subtraí-los, multiplicá-los ou dividí-los{cores.fim}')
print(separador)

while True:
    try:
        valor1 = int(input(f'{cores.verde}Digite o primeiro valor: {cores.amarelo}').strip())
        print()
        break
    except ValueError:
        print(f'{cores.vermelho}\nEntrada inválida.\n')

while True:
    try:
        valor2 = int(input(f'{cores.verde}Digite o segundo valor: {cores.amarelo}').strip())
        break
    except ValueError:
        print(f'{cores.vermelho}\nEntrada inválida.\n')

while True:
    try:

        print(separador)
        print(f'{cores.verde}Opções:\n\n   [ 1 ] - Somar\n   [ 2 ] - Subtrair\n   [ 3 ] - Multiplicar\n   [ 4 ] - Dividir\n   [ 5 ] - Maior e menor\n   [ 6 ] - Novos números\n   [ 7 ] - Finalizar programa\n')

        while True:
            try:
                escolha = int(input(f'{cores.verde}Escolha: {cores.amarelo}').strip())
                if escolha in [1,2,3,4,5,6,7]:
                    break
                else:
                    print(f'{cores.vermelho}\nDigite uma das opções disponíveis.\n')
            except ValueError:
                print(f'{cores.vermelho}\nEntrada inválida.\n')

        print(separador)

        if escolha == 1:
            print(f'{cores.amarelo} A soma dos valores {valor1} e {valor2} é igual a {valor1+valor2}.')

        elif escolha == 2:
            print(f'{cores.amarelo} {valor1} menos {valor2} é igual a {valor1-valor2} e {valor2} menos {valor1} é igual a {valor2 - valor1}.')

        elif escolha == 3:
            print(f'{cores.amarelo} A multiplicação de {valor1} por {valor2} é igual a {valor1*valor2}.')

        elif escolha == 4:
            print(f'{cores.amarelo} A divisão de {valor1} por {valor2} é igual a {valor1/valor2} e a divisão de {valor2} por {valor1} é igual a {valor2/valor1}.')

        elif escolha == 5:
            if valor1 > valor2:
                print(f'{cores.amarelo} O maior valor é o {valor1} e o menor é o {valor2}.')
            elif valor1 < valor2:
                print(f'{cores.amarelo} O maior valor é o {valor2} e o menor é o {valor1}.')
            else:
                print(f'{cores.amarelo} Os valores são iguais.')

        elif escolha == 6:
            while True:
                try:
                    valor1 = int(input(f'{cores.amarelo}Digite o primeiro valor: {cores.ciano}').strip())
                    print()
                    break
                except ValueError:
                    print(f'{cores.vermelho}\nEntrada inválida.\n')

            while True:
                try:
                    valor2 = int(input(f'{cores.amarelo}Digite o segundo valor: {cores.ciano}').strip())
                    break
                except ValueError:
                    print(f'{cores.vermelho}\nEntrada inválida.\n')

        elif escolha == 7:
            while True:
                try:
                    confirmacao = input(f'{cores.amarelo} Confirma? [S/N] :{cores.verde}').strip().upper()
                    if confirmacao not in ['S','N']:
                        print(f'{cores.vermelho}\nEntrada inválida.\n')
                    else:
                        break
                except ValueError:
                    print(f'{cores.vermelho}\nEntrada inválida.\n')
            if confirmacao == 'S':
                print(f'{cores.verde}\nPrograma finalizado.\n')
                break

    except ValueError:
        print(f'{cores.vermelho}\nEntrada inválida.\n')