
numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    try:
        n = int(input('\nDigite um número para vê-lo por extenso: '))
        if n < 0 or n > 20:
            print('\nDigite um número de 0 a 20.')
        else:
            print()
            break
    except ValueError:
        print('\nEntrada inválida.')

print(f'O número {n} por extenso fica como "{numeros[n]}"\n')