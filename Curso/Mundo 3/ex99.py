def maior(*numbers):

    for number in numbers:
        if number == numbers[0]:
            maior_numero = number
        if number > maior_numero:
            maior_numero = number
    
    print(f'\nO maior número é {maior_numero}\n')
    return maior_numero
            
maior(544,235,653,234,56,54,345,23,635,675,786,564,54,23,45,6745,345,675,453,23,453,456,76,786,345,25,44756,746,45,2523,2,3556,7456,34,2354,4523,657,345,457,5678,54,346)