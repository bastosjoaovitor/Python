def texto(msg):
    linha = len(msg) + 4
    print(linha*'~')
    print(f'{msg:^{linha}}')
    print(linha*'~')
def digitar(msg):
    from time import sleep
    for caractere in msg:
        print(caractere, end='', flush=True)
        sleep(0.05)

while True:

    print('\033[m\033[37;42m')
    texto('SISTEMA DE AJUDA PyHelp')
    print('\033[m')

    comando = input('Digite o nome do comando que você deseja\nobter ajuda ["fim" para finalizar o programa] : ').lower()

    if comando == 'fim':
        digitar('\nFinalizando programa...\n\nAdeus\n\n')
        exit()
    elif comando == '':
        continue
    else:
        print('\033[7m', end='')
        help(comando)
