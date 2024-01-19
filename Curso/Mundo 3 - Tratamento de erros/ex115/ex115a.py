import sqlite3
from bibliotecaex155 import addnome, titulo, digitar
from time import sleep
# bibliotecas

caminho_do_banco_de_dados = 'Python/Curso/Mundo 3 - Tratamento de erros/ex115/databaseex115a.db'
conexao = sqlite3.connect(caminho_do_banco_de_dados)
cursor = conexao.cursor()
# banco de dados e cursor

class cores:
    verde = '\033[32m'
    ciano = '\033[36m'
    vermelho = '\033[31m'
    fim = '\033[m'
# cores

while True:

    print(cores.fim, end='')
    print()
    titulo('CADASTRO')
    # titulo

    print(f'''
[ {cores.verde}1{cores.fim} ] - {cores.ciano}Ver pessoas cadastradas{cores.fim}
[ {cores.verde}2{cores.fim} ] - {cores.ciano}Cadastrar nova pessoa{cores.fim}
[ {cores.verde}3{cores.fim} ] - {cores.ciano}Sair do sistema{cores.fim}''')
    # opções

    while True:
        try:
            opcao = input(f'\n{cores.ciano}Sua opção: {cores.verde}').strip()
            opcao = int(opcao)
            if opcao not in [1,2,3]:
                digitar(f'\n{cores.vermelho}Erro! {opcao} não é um opção existente, por favor, digite 1, 2 ou 3.\n', 0.03)
                continue
            break
        except:
            digitar(f'\n{cores.vermelho}Erro! "{opcao}" não é uma opção, por favor, digite 1, 2 ou 3.\n', 0.03)
    # escolha do usuario

    if opcao == 1:

        print(cores.fim)
        titulo('Pessoas cadastradas', '=')
        sleep(0.5)

        digitar(f'\n{30*'-'}\n', 0.01)
        digitar(f'{'índice |':<11}{'nome':<19}\n', 0.03)
        digitar(f'{30*'-'}\n', 0.01)

        cursor.execute("SELECT * FROM registro;")

        resultados = cursor.fetchall()

        for resultado in resultados:
            print(f'{resultado[0]:<11}{resultado[1]:<19}')
            #print(resultado[0])
            sleep(0.2)
        digitar(f'{30*'-'}\n', 0.01)
        sleep(2)
        print()
        print(30*"=")
    # Ver pessoas cadastradas

    if opcao == 2:

        print(cores.fim, end='')
        while True:
            nome = input(f'\n{cores.ciano}Digite o nome da pessoa: {cores.verde}').strip()
            if nome == '':
                print(f'\n{cores.vermelho}Por favor, digite um nome.')
                continue
            if len(nome) > 19:
                print(f'\n{cores.vermelho}Nome muito grande, limite de 19 caracteres.')
                continue
            break
        addnome(nome)
    # adicionar pessoa

    if opcao == 3:

        print()
        digitar(30*"=", 0.01)
        digitar(f'\n\nFinalizando programa')
        digitar('...', 0.5)
        digitar('\n\nTenha um bom dia!\n\n')
        conexao.close()
        break
    # finalizar programa

    