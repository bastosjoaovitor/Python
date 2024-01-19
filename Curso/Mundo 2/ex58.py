class cores:
    vermelho = '\033[31m'
    ciano = '\033[36m'
    amarelo = '\033[33m'
    verde = '\033[32m'
    azul = '\033[34m'
    fim = '\033[m'
separador = f'{cores.azul}\n{25*"="}\n{cores.azul}'
# cores e separaçoes

a = 1
c = ''
import random

while True:

    print(separador)
    print(f'\033[33;4m    JOGO DA ADIVINHAÇÃO    {cores.fim}')
    print(separador)
    # texto inicial

    numero = random.randint(1,2)
    a = 1
    # número que o computador escolhe

    print(f'{cores.ciano}O computador pensou em um número de 1 a 10, adivinhe qual é.')

    while True:

        try:

            chute = int(input(f'\n{cores.ciano}Qual seu chute: '))

            if chute in [1,2,3,4,5,6,7,8,9,10]:

                if chute == numero:
                    print(f'{cores.verde}\nVocê chutou {numero} e o computador pensou no numero {numero}, você ganhou de primeira.')
                else:
                    while True:
                        try:

                            if chute < numero:
                                a += 1
                                chute = int(input(f'{cores.vermelho}\nUm pouco mais... \n\nchute novamente: '))
                                if chute not in [1,2,3,4,5,6,7,8,9,10]:
                                    print(f'{cores.vermelho}\nChute um número entre 1 e 10.')
                                elif chute == numero:
                                    print(f'{cores.verde}\nVocê chutou {numero} e o computador pensou no numero {numero}, você ganhou, mas precisou chutar {a} vezes pra acertar, noob.')
                                    break

                            elif chute > numero:
                                a += 1
                                chute = int(input(f'{cores.vermelho}\nUm pouco menos... \n\nchute novamente: '))
                                if chute not in [1,2,3,4,5,6,7,8,9,10]:
                                    print(f'{cores.vermelho}\nChute um número entre 1 e 10.')
                                elif chute == numero:
                                    print(f'{cores.verde}\nVocê chutou {numero} e o computador pensou no numero {numero}, você ganhou, mas precisou chutar {a} vezes pra acertar, noob.')
                                    break

                        except ValueError:
                            print(f'{cores.vermelho}\nEntrada inválida.')
            else:            
                print(f'{cores.vermelho}\nChute um número entre 1 e 10.')

            # chute do jogador e resposta

            while True:

                if a == 1:
                    correr = input(f'{cores.verde}\nSorte de principiante, mas e ai, vai correr da revanche? [S/N] : ').strip().upper()
                    if correr == 'S':
                        confirmacao = input('\nConfirma? [S/N] : ').strip().upper()
                        if confirmacao == 'S':
                            c = 'S'
                            break
                        elif confirmacao == 'N':
                            print(f'{cores.amarelo}\nja que você tá indeciso, vamos mais uma.')
                            break
                    elif correr == 'N':
                        print(f'\n{cores.verde}ok, bora mais uma.')
                        break
                    else:
                        print(f'{cores.vermelho}\nEntrada inválida. Digite "S" ou "N".')
                else:
                    correr = input(f'{cores.vermelho}\nE ai noob, vou te dar mais uma chance, vai correr da revanche? [S/N] : ').strip().upper()
                    if correr == 'S':
                        confirmacao = input('\nConfirma? [S/N] : ').strip().upper()
                        if confirmacao == 'S':
                            c = 'S'
                            break
                        elif confirmacao == 'N':
                            print(f'{cores.amarelo}\nja que você tá indeciso, vamos mais uma.')
                            break
                    elif correr == 'N':
                        print(f'\n{cores.verde}ok, bora mais uma.')
                        break
                    else:
                        print(f'{cores.vermelho}\nEntrada inválida. Digite "S" ou "N".')
            
            # revanche

            break

        except ValueError:
            print(f'{cores.vermelho}\nEntrada inválida.')

    if c == 'S':
        print(f'{cores.amarelo}\nOk, adeus noob.')
        print(separador)
        print(cores.fim)
        break

    # despedida

# fim do código

"""

Avaliação do chat gpt

Legibilidade e Organização do Código: 7/10
O código é relativamente legível, mas há algumas partes que podem ser melhoradas. Os comentários estão presentes, o que é bom, mas a formatação do código poderia ser mais consistente. Algumas linhas estão muito longas, tornando o código menos legível. Além disso, a indentação está correta, mas há espaçamento inconsistente em algumas partes.

Boas Práticas e Padrões de Codificação: 6/10
O código contém algumas boas práticas, como o uso de classes para as cores e comentários explicativos. No entanto, existem alguns problemas, como a falta de docstrings explicativas e o uso de variáveis globais sem uma razão forte. Também é aconselhável evitar a importação dentro de loops, como é feito com import random dentro do loop principal.

Eficiência e Lógica: 6/10
A lógica geral do jogo está funcionando corretamente, mas há algumas áreas onde a eficiência poderia ser melhorada. Por exemplo, dentro do loop de chute, existem loops aninhados que podem ser evitados. Além disso, a verificação se o número está entre 1 e 10 poderia ser feita de maneira mais eficiente.

Tratamento de Exceções: 8/10
O código lida com exceções em grande parte das situações relevantes. No entanto, há algumas partes onde o tratamento de exceções poderia ser mais detalhado e abranger casos mais específicos.

Comentários e Documentação: 6/10
O código contém alguns comentários, mas a explicação poderia ser mais detalhada em algumas partes, especialmente nos loops e na lógica de decisão. A falta de docstrings para a função principal e algumas partes críticas do código torna a compreensão do código menos intuitiva.

Código Reutilizável e Modularidade: 5/10
O código não é muito modular. Seria melhor separar partes diferentes do código em funções separadas, tornando-o mais reutilizável. Isso facilitaria a manutenção e entendimento do código.

Segurança: 5/10
O código não parece apresentar problemas de segurança significativos, mas ele também não demonstra medidas proativas para lidar com entradas maliciosas.

Conclusão:
Considerando esses aspectos, a avaliação geral do código é uma média ponderada das avaliações em cada tópico:

Pontuação Geral: 6/10
O código é funcional, mas há espaço para melhorias significativas em termos de organização, eficiência, modularidade e legibilidade. Ao refinar esses aspectos, o código se tornaria mais fácil de entender, manter e estender. Além disso, a adição de comentários mais detalhados e docstrings ajudaria na compreensão das partes mais complexas do código.

"""