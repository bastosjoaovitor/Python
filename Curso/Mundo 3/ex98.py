from time import sleep

def contador():
    print(30*"-")
    print('CONTAGEM DE 1 ATÉ 10 DE 1 EM 1\n')
    for a in range(1,11):
        print(a, end=' ', flush=True)
        sleep(0.1)
    print()
    print(30*"-")
    print('CONTAGEM DE 10 ATÉ 0 DE 2 EM 2\n')
    for a in range(10,-1, -2):
        print(a, end=' ', flush=True)
        sleep(0.1)
    print()
    print(30*"-")
    print('CONTAGEM DE X ATÉ Y DE Z EM Z')
    while True:
        try:
            X = int(input('\nX : '))
            break
        except ValueError:
            continue
    while True:
        try:
            Y = int(input('\nY : '))
            break
        except ValueError:
            continue
    while True:
        try:
            Z = int(input('\nZ : '))
            if Z == 0:
                Z = 1
            if X > Y:
                if Z > 0:
                    Z = Z - (Z*2)
            elif X < Y:
                if Z < 0:
                    Z = Z - (Z*2)
            break
        except ValueError:
            continue
    print()
    if X > Y:
        for a in range(X, Y-1, Z):
            print(a, end=' ', flush=True)
            sleep(0.1)
    elif X < Y:
        for a in range(X, Y+1, Z):
            print(a, end=' ', flush=True)
            sleep(0.1)
    elif X == Y:
        print(X)
    print()
    print(30*"-")

print()
contador()
print()