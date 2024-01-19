print(f'\n{25*"-="}\nAnalisador de Triángulos\n{25*"-="}\n')
s1 = float(input('Primeiro segmento: '))
s2 = float(input('\nSegundo segmento: '))
s3 = float(input('\nTerceiro segmento: '))
print(f'\n{25*"-="}\n')
if s1 + s2 > s3:
    print('Os segmentos acima podem formar um triângulo.')
else:
    print('Os segmentos acima não podem formar um triângulo.')
print(f'\n{25*"-="}\n')