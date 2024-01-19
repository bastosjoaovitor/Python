frase = str(input('Digite uma frase para saber se ela é um palíndromo: \n\n'))
frase = frase.replace(' ','')

fraseinvertida = ''
for c in range(len(frase) - 1, - 1, - 1):
    fraseinvertida = fraseinvertida + frase[c]

if frase == fraseinvertida:
    print(f'\nA frase "{frase}" é um palíndromo, invertida fica como "{fraseinvertida}", que é igual a frase normal.\n')
else:
    print(f'\nA frase não é um palíndromo, pois normal é "{frase}", e invertida fica como "{fraseinvertida}".\n')