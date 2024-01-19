tabela = ('Botafogo', 'Bragantino', 'Grêmio', 'Palmeiras', 'Flamengo', 'Fluminense', 'Atlético-MG', 'Atlético-PR', 'Fortaleza', 'São Paulo', 'Cuiabá', 'Cruzeiro', 'Corinthias', 'Internacional', 'Santos', 'Goiás', 'Vasco da gama', 'Bahia', 'América-MG', 'Coritiba')

separador = f'\n{25*"=-"}=\n'
from time import sleep

c = 'N'

print(separador)
print(f'{"BRASILEIRÃO":^50}')
print(separador)


while c == 'N':

    print("""Selecione umas das opções:\n
[ 1 ] - 5 primeiros colocados
[ 2 ] - 4 últimos colocados
[ 3 ] - Times em ordem alfabética
[ 4 ] - Sair do programa""")
    
    while True:
        try:
            escolha = int(input('\nOpção: '))
            if escolha in [1,2,3,4]:
                break
            else:
                print('\nEscolha uma das opções.')
        except ValueError:
            print('\nEntrada inválida.')

    if escolha == 1:
        print(separador)
        print('Os 5 primeiros colocados são:', end='')
        for a in range(0,5):
            if a == 4:
                print(f' e {tabela[a]}.\n')
            else:
                print(f' {tabela[a]},', end='')

    elif escolha == 2:
        print(separador)
        print('Os 4 últimos colocados são: Vasco da gama, Bahia, América-MG, e Coritiba.\n')

    elif escolha == 3:
        print(separador)
        print(sorted(tabela))
        print()

    else:
        while True:
            try:
                c = input('\nConfirma [S/N]: ').upper().strip()[0]
                if c in ['S','N']:
                    print()
                    break
                else:
                    print('\nDigite "S" para sair do programa ou "N" para continuar.')
            except ValueError:
                print('\nEntrada inválida.')

mensagem = "Finalizando..."

for letra in mensagem:
    print(letra, end='', flush=True)
    sleep(0.1)

print('\n')