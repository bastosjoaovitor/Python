from math import sin, cos, tan, radians
print(f'\n{20*"="}\n')
a = float(input('Digite o ângulo que você deseja: '))
print(f'\n{20*"="}\n\nO seno desse ângulo é {sin(radians(a)):.2f}.\nO cosseno é {cos(radians(a)):.2f}.\nA tangente é {tan(radians(a)):.2f}.\n\n{20*"="}\n')