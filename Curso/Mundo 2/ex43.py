class cores:
    azul = "\033[34m"
    amarelo = "\033[33m"
    verde = "\033[32m"
    vermelho = "\033[31m"
    branco = "\033[37m"
    fim = "\033[m"
separador = f'{cores.azul}\n{25*"-="}\n{cores.fim}'
# melhorar legibilidade

print(separador)
print('\033[33mCalcule seu imc')
print(separador)
# texto inicial

while True:
    try:
        peso = float(input(f'{cores.amarelo}Digite seu peso (kg): {cores.branco}'))
        break
    except ValueError:
        print(f'{cores.vermelho}\nEntrada inválida.\n')

while True:
    try:
        altura = float(input(f'{cores.amarelo}\nDigite sua altura (M): {cores.branco}'))
        break
    except ValueError:
        print(f'{cores.vermelho}\nEntrada inválida.')

imc = peso / altura ** 2
# peso e altura

if imc < 18.5:
    print(f'{cores.vermelho}\nSeu imc é de {imc:.1f}, você está abaixo do peso.')
elif imc < 25:
    print(f'{cores.verde}\nSeu imc é de {imc:.1f}, você está no peso normal.')
elif imc < 30:
    print(f'{cores.amarelo}\nSeu imc é de {imc:.1f}, você está com sobrepeso.')
elif imc < 35:
    print(f'{cores.vermelho}\nSeu imc é de {imc:.1f}, o que configura obesidade grau I.')
elif imc < 40:
    print(f'{cores.vermelho}\nSeu imc é de {imc:.1f}, o que configura obesidade grau II.')
else:
    print(f'{cores.vermelho}\nSeu imc é de {imc:.1f}, o que configura obesidade grau III.')
# resposta

print(separador)
#fim