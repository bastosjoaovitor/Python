dados = []
opcao = ''
adicionar_aluno = 'S'
finalizar_programa = 'N'

from time import sleep

print(f'\n{20*"=-"}=')
print(f'{"\033[4mNota dos alunos\033[m":^48}')
print(f'{20*"=-"}=\n')

while finalizar_programa != 'S':

    while adicionar_aluno != 'N':

        nome_e_nota_do_aluno = []

        while True:

            nome_do_aluno = input('\nNome do aluno(a): ')
            if nome_do_aluno == '':
                print('\nEntrada inválida.')
            else:
                nome_e_nota_do_aluno.append(nome_do_aluno)
                break
        
        while True:
            
            try:
                nota_1 = int(input('\nNota 1: '))
                if nota_1 < 0:
                    print('\nA nota não pode ser menor que zero.')
                elif nota_1 > 10:
                    print('\nA nota não pode ser maior que 10')
                else:
                    nome_e_nota_do_aluno.append(nota_1)
                    break
            except ValueError:
                print('\nEntrada inválida.')

        while True:
            
            try:
                nota_2 = int(input('\nNota 2: '))
                if nota_2 < 0:
                    print('\nA nota não pode ser menor que zero.')
                elif nota_2 > 10:
                    print('\nA nota não pode ser maior que 10')
                else:
                    nome_e_nota_do_aluno.append(nota_2)
                    break
            except ValueError:
                print('\nEntrada inválida.')

        dados.append(nome_e_nota_do_aluno[:])

        while True:

            adicionar_aluno = input('\nAdicionar outro aluno(a) [S/N]: ')
            if adicionar_aluno == '':
                continue
            else:
                adicionar_aluno = adicionar_aluno.upper()
                if adicionar_aluno in ['S','N']:
                    break
            
    print(f'\n{20*"=-"}=\n')
    print(f'{41*"-"}')
    print(f'{"Nº":<10}', end='')
    print(f'{"NOME":<10}', end='')
    print(f'{"MÉDIA":>20}')
    print(f'{41*"-"}')

    for posicao, info in enumerate(dados):

        print(f'{posicao:<10}', end='')
        print(f'{info[0]:<10}', end='')
        print(f'{(info[1] + info[2]) / 2:>20}')

    print(f'{41*"-"}')
    print(f'\n{20*"=-"}=')

    while finalizar_programa not in ['S','Y']:

        print('''\nEscolha uma das opções:
       
[ 1 ] - Mostrar lista
[ 2 ] - Mostrar notas e média de um aluno
[ 3 ] - Reiniciar programa
[ 4 ] - Finalizar programa''')
        
        while True:

            opcao = input('\nOpção: ')
            if opcao in ['1','2','3','4']:
                break
            else:
                print('\nOpção inválida, digite 1, 2, 3 ou 4.')

        if opcao == '1':

            print(f'\n{20*"=-"}=\n')
            print(f'{41*"-"}')
            print(f'{"Nº":<10}', end='')
            print(f'{"NOME":<10}', end='')
            print(f'{"MÉDIA":>20}')
            print(f'{41*"-"}')

            for posicao, info in enumerate(dados):

                print(f'{posicao:<10}', end='')
                print(f'{info[0]:<10}', end='')
                print(f'{(info[1] + info[2]) / 2:>20}')

            print(f'{41*"-"}')
            print(f'\n{20*"=-"}=\n')

        elif opcao == '2':

            while True:

                try:

                    numero_do_aluno = int(input('\nDigite a posição do aluno na lista [digite -1 para voltar ao menu] : '))

                    if numero_do_aluno >= len(dados) or numero_do_aluno < -1:
                        print('\nNão tem um aluno com essa posição na lista.')
                    elif numero_do_aluno == -1:
                        break
                    else:
                        print(f'\n{65*"-"}')
                        print(f'O aluno {dados[numero_do_aluno][0]} tirou as notas {dados[numero_do_aluno][1]} e {dados[numero_do_aluno][2]}, ficando com média de {(dados[numero_do_aluno][1] + dados[numero_do_aluno][2]) / 2}')
                        print(f'{65*"-"}')
                        break
                except ValueError:
                    print('\nEntrada inválida.')

        elif opcao == '3':

            dados = []
            opcao = ''
            adicionar_aluno = 'S'

            print(f'\n{20*"=-"}=')
            print(f'{"\033[4mNota dos alunos\033[m":^48}')
            print(f'{20*"=-"}=\n')
            break

        elif opcao == '4':

            while True:

                finalizar_programa = input('\nConfirma [S/N] : ')
                if finalizar_programa == '':
                    print('\nDigite "S" ou "N".')
                    continue
                else:
                    finalizar_programa = finalizar_programa.upper()
                    if finalizar_programa in ['S','N']:
                        break
                    else:
                        print('\nDigite "S" ou "N".')

fim = 'Finalizando programa...'
adeus = 'Adeus'

print()

for letra in fim:
    
    print(letra, end='', flush=True)
    sleep(0.05)

print('\n')

for letra in adeus:
    
    print(letra, end='', flush=True)
    sleep(0.05)

print('\n')