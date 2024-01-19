
print(' \nWhile ')

while True:
    escolha = input('\nDeseja reiniciar o programa [S/N] : ').upper().strip()
    if escolha != 'S' and escolha != 'N':
        print('entrada inválida.')
    elif escolha == 'S':
        print(' \nWhile ')
    else:
        confirmacao = input('\nConfirma [S/N]: ').upper().strip()
        if confirmacao == 'S':
            print('\nPrograma finalizado.\n')
            break
        elif confirmacao != 'N':
            print('Entrada inválida.\n')

            