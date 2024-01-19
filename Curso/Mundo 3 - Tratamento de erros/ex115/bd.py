import sqlite3

caminho_do_banco_de_dados = 'Python/Curso/Mundo 3 - Tratamento de erros/ex115/databaseex115a.db'

conexao = sqlite3.connect(caminho_do_banco_de_dados)

cursor = conexao.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS registro (id INTEGER PRIMARY KEY, nome TEXT NOT NULL)''')

cursor.execute("INSERT INTO registro (nome) VALUES ('Pedro')")
cursor.execute("INSERT INTO registro (nome) VALUES ('Maria')")
cursor.execute("INSERT INTO registro (nome) VALUES ('Gabriel')")
cursor.execute("INSERT INTO registro (nome) VALUES ('Mateus')")
cursor.execute("INSERT INTO registro (nome) VALUES ('Ana')")
cursor.execute("INSERT INTO registro (nome) VALUES ('Luiza')")
cursor.execute("INSERT INTO registro (nome) VALUES ('Kaua')")
cursor.execute("INSERT INTO registro (nome) VALUES ('Vitória')")

conexao.commit()

