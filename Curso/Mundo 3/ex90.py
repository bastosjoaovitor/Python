dados = {}

while True:
    
    nome = input('\nNome do aluno: ')
    if nome != '':
        dados['nome'] = nome
        break

while True:
    
    try:
        media = int(input('\nMédia: '))
        if 0 <= media <= 10:
            dados['media'] = media
            if media == 0:
                dados['situacao'] = 'Burro'
            elif 0 < media < 7:
                dados['situacao'] = 'Reprovado'
            else:
                dados['situacao'] = 'Aprovado'
            break
        else:
            print('\nA média do aluno não pode ser menor que 0 ou maior que 10')

    except ValueError:
        print('\nEntrada inválida.')

print(f'\nNome: {dados["nome"]}\nMédia: {dados["media"]}\nSituação do aluno: {dados["situacao"]}.\n')