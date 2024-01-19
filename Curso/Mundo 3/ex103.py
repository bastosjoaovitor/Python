def ficha():
    """

    => Faz a ficha do jogador.
    :param name: O nome do jogador
    :param goals: Quantidade de gols que o jogador fez
    :return: Ficha
    """

    name = input('\nNome do jogador: ').title()
    if name == '':
        name = 'Desconhecido'

    while True:
        try:
            goals = input(f'\nQuantos gols o jogador "{name}" fez: ')
            if goals.isnumeric() == True:
                goals = int(goals)
                if goals < 0:
                    goals = 0
                break
            else:
                if goals == '':
                    goals = 0
                    break
                else:
                    print('\nEntrada inválida.')
        except ValueError:
            if goals == '':
                goals = 0
                break
            print('\nEntrada inválida.')
        
    print(f'\nO jogador "{name}" fez {goals} gols no campeonato.\n')

ficha()