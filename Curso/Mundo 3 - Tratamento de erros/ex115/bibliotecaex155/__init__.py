def addnome(name):
    '''
    => Adiciona um nome ao banco de dados do exercício.
    :param name: O nome que será adicionado.
    '''
    import sqlite3
    caminho_do_banco_de_dados = 'Python/Mundo 3 - Tratamento de erros/ex115/databaseex115a.db'
    conexao = sqlite3.connect(caminho_do_banco_de_dados)
    cursor = conexao.cursor()
    cursor.execute(f"INSERT INTO registro (nome) VALUES ('{name}')")
    conexao.commit()
    conexao.close()

def titulo(msg, separador = '-'):
    '''
    => Manda a mensagem em título, com separadores.
    :param msg: Título.
    :param separador: Caractere que aparece em sequência abaixo e acima do título.
    '''
    print(30* f"{separador}")
    print(f'{msg:^30}')
    print(30* f"{separador}")

def digitar(msg, intervalo = 0.05):
    '''
    => Efeito de digitação.
    :param msg: Mensagem que será digitada.
    :param intervalo: intervalo de tempo que cada caractere demora pra aparecer na tela.
    '''
    from time import sleep
    for caractere in msg:
        print(caractere, end='', flush=True)
        sleep(float(intervalo))

