from random import randint

def digite(msg):
    from time import sleep
    for caractere in msg:
        print(caractere, end='', flush=True)
        sleep(0.05)
    
def somarlista(*numbers):
    pares = []
    for numero in numbers:
        if numero % 2 == 0:
            pares.append(numero)
    somadospares = sum(pares)
    digite(f'\nSomando os valores pares de {numbers}, temos {somadospares}\n')

somarlista(randint(0,1000),randint(0,1000),randint(0,1000),randint(0,1000),randint(0,1000))