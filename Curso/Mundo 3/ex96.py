def area(largura, altura):
    area = largura * altura
    return area

Area = area(int(input('\nLargura: ')), int(input('\nAltura: ')))

print(f'\nA área é igual a {Area}m²\n')