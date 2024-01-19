print(f'\n{20*"="}\n')
frase = str(input('Digite uma frase: ')).strip().lower()
letra = str(input('\nAgora digite uma letra, e o programa irá te dizer quantas vezes essa letra\naparece e qual é a primeira e última posição que essa letra aparece na frase.\n\nLetra: ')).strip().lower()
letra = letra[0]
print(f'\n{20*"="}\n')
print(f'A letra {letra.upper()} aparece {frase.count(letra)} vezes na sua frase.')
print(f'A primeira letra {letra.upper()} apareceu na posição {frase.find(letra)+1}.')
print(f'A última letra {letra.upper()} apareceu na posição {frase.rfind(letra)+1}.')
print(f'\n{20*"="}\n')