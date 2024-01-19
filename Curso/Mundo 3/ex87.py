matriz = [[],[],[]]
soma_valores_pares = 0
soma_valores_terceira_coluna = 0
maior_valor_segunda_linha = 0

print(f'\n{40*"="}\n\n{"\033[4mMATRIX 3X3\033[m":^46}\n\n{40*"="}')

for c in range(1,4):
    
    for z in range(1,4):

        while True:

            try:

                if c == 1 and z == 1:
                    valor = int(input(f'\nDigite um número para posição [{c},{z}]: '))
                else:
                    valor = int(input(f'\nMais um para posição [{c},{z}]: '))

                matriz[c-1].append(valor)

                if valor % 2 == 0:
                    soma_valores_pares += valor

                if z == 3:
                    soma_valores_terceira_coluna += valor

                if c == 2:
                    if valor > maior_valor_segunda_linha:
                        maior_valor_segunda_linha = valor

                break

            except ValueError:
                print('\nEntrada inválida.')

print(f'\n{40*"="}\n\nA matriz fica assim:\n\n{matriz[0]}\n{matriz[1]}\n{matriz[2]}\n\nA soma dos valores pares digitados é igual a {soma_valores_pares}\n\nA soma dos valores da terceira coluna é igual a {soma_valores_terceira_coluna}\n\nE o maior valor da segunda linha é {maior_valor_segunda_linha}\n\n{40*"="}\n\nPrograma finalizado.\n')