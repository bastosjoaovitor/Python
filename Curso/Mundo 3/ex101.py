from datetime import datetime

def votar(ano_de_nascimento):
    global idade
    idade = datetime.now().year - ano_de_nascimento
    if 18> idade > 15 or idade > 70:
        situacao = 'VOTO OPCIONAL.'
    elif idade < 16:
        situacao = 'NÃO PODE VOTAR.'
    else:
        situacao = 'VOTO OBRIGATÓRIO.'
    return situacao

print(), print(30*"-")
ano_de_nascimento = int(input('Ano de nascimento: '))
voto = votar(ano_de_nascimento)
print(f'\nCom {idade} anos: {voto}\n')