print('')
print('----------------------------')
print('')
n1 = float(input('DIGITE UM NÚMERO: '))
n2 = float(input('DIGITE OUTRO: '))  
s = n1 + n2
print('')
print('A soma de {} mais {} é igual a {}'.format(n1,n2,s))
print('')
print('----------------------------')
print('')
print('Sobre o primeiro número que você escolheu, o {}, informações: '.format(n1))
print('')
print('O tipo primitivo desse valor é ', type(n1))
print('')
print('{} é ASCII? '.format(n1), n1.isascii())
print('{} é alfanumérico ? '.format(n1), n1.isalnum())
print('{} é letra? '.format(n1), n1.isalpha())
print('{} é decimal? '.format(n1), n1.isdecimal())
print('{} é um dígito? '.format(n1), n1.isdigit())
print('{} é identifier? '.format(n1), n1.isidentifier())
print('{} é numérico? '.format(n1), n1.isnumeric())
print('{} pode ser impresso? '.format(n1), n1.isprintable())
print('{} é um espaço? '.format(n1), n1.isspace())                                                         # Dessa forma, a soma e o tipo primitivo funcionam, mas o resto não. #
print('{} está somente em letras minúsculas? '.format(n1), n1.islower())
print('{} está somente em letras maiúsculas? '.format(n1), n1.isupper())
print('{} tem letras maiúsculas e letras minúsculas? '.format(n1), n1.istitle())
print('')
print('----------------------------')
print('')
print('Sobre o segundo número que você escolheu, o {}, informações: '.format(n2))
print('')
print('O tipo primitivo desse valor é ', type(n2))
print('')
print('{} é ASCII?'.format(n2), n2.isascii())
print('{} é alfanumérico ? '.format(n2), n2.isalnum())
print('{} é letra? '.format(n2), n2.isalpha())
print('{} é decimal? '.format(n2), n2.isdecimal())
print('{} é um dígito? '.format(n2), n2.isdigit())
print('{} é identifier? '.format(n2), n2.isidentifier())
print('{} é numérico? '.format(n2), n2.isnumeric())
print('{} pode ser impresso? '.format(n2), n2.isprintable())
print('{} é um espaço? '.format(n2), n2.isspace())
print('{} está somente em letras minúsculas? '.format(n2), n2.islower())
print('{} está somente em letras maiúsculas? '.format(n2), n2.isupper())
print('{} tem letras maiúsculas e letras minúsculas? '.format(n2), n2.istitle())
print('')
print('----------------------------')
print('')