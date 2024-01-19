palavras = ('estampar', 'luso', 'desodorante', 'iniquidade', 'cinzelado', 'calamidade', 'confiabilidade', 'abacaxi', 'isca', 'examinado')

vogais = ('a','e','i','o','u')

for p in palavras:
    print(f'\nA palavra "{p.upper()}" tem as vogais:', end='')
    for v in vogais:
        if v in p:
            print(f' {v.upper()}', end='')
    print()

print()