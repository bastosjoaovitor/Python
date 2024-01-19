def nota(notas = [], sit=False):
    '''
    => Lê as notas da sala e gera um dicionário com os dados
        :param notas: Notas dos alunos
        :param sit: (opcional) Mostrar ou não a situação dos alunos
    '''

    dados = {'quantidade de notas': 0, 'maior nota': -1, 'menor nota': 100, 'media': 0}

    for nota in notas:
        dados['quantidade de notas'] += 1
        if nota > dados['maior nota']:
            dados['maior nota'] = nota
        if nota < dados['menor nota']:
            dados['menor nota'] = nota
        dados['media'] += nota

    dados['media'] = dados['media'] / dados['quantidade de notas']

    if sit == True:
        if dados['media'] < 6:
            dados['situacao'] = 'REPROVADOS'
        else:
            dados['situacao'] = 'APROVADOS'
    
    return dados

notas = []

continuar = 'S'
while continuar == 'S':

    while True:

        try:
            a = int(input('\nNota: '))
            if -1 < a < 11:
                notas.append(a)
                break
        except ValueError:
            print('\n\033[31mEntrada inválida.\033[m')

    while True:
        
        continuar = input('\nAdicionar outra? [S/N] : ').title()
        if continuar in ['S','N']:
            break

while True:

    sit = input('\nDeseja saber a situação geral da turma? [S/N] : ').title()
    if sit == 'S':
        sit = True
        break
    elif sit == 'N':
        sit = False
        break

dados = nota(notas, sit)

print(f'''
- Quantidade de notas: {dados['quantidade de notas']}
- Maior nota: {dados["maior nota"]}
- Menor nota: {dados["menor nota"]}
- Média da turma: {dados["media"]}''')
if len(dados) == 5:
    print(f'- Situação geral da turma: {dados["situacao"]}\n')
else:
    print()