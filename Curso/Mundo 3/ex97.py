def escreva(msg):
    n = len(msg) + 4
    print(n*"-")
    print(f'{msg:^{n}}')
    print(n*"-")

escreva(input('\nDigite algo: '))