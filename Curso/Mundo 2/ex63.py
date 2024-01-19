class cores:
    vermelho = '\033[31m'
    amarelo = '\033[33m'
    verde = '\033[32m'
    azul = '\033[34m'
    fim = '\033[m'
separador = f'{cores.azul}\n{25*"="}\n{cores.fim}'
# Cores e separaçoes

print(separador)
print(f'\033[33;4m    Sequência de Fibonacci    {cores.fim}')
print(separador)
# Texto inicial

while True:
    try:
        termos = int(input(f'Quantos termos quer ver: '))
        if termos < 1:
            print(f'{cores.vermelho}\nSomente número positivos.\n{cores.fim}')
        else:
            break
    except ValueError:
        print(f'{cores.vermelho}\nEntrada inválida.\n{cores.fim}')
# Pergunta ao usuário quantos termos mostrar

primeiro_termo = 1
segundo_termo = 1
soma = 2
# Primeiros termos da Sequência de Fibonacci

for c in range(1,termos+1):
    if segundo_termo == 1:
        print(f'{cores.verde}\n0 => 1 => 1 => ', end='')
        soma = primeiro_termo + segundo_termo
        segundo_termo = soma
        primeiro_termo = soma - primeiro_termo
    else:
        print(f'{soma} => ', end='')
        soma = primeiro_termo + segundo_termo
        segundo_termo = soma
        primeiro_termo = soma - primeiro_termo
print(soma)
# Mostrando a quantidade de termos escolhidos

print(separador)
# Fim