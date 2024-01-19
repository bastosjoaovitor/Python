class Cliente():
    def __init__(self, nome, email, plano):
        self.nome = nome
        self.email = email
        self.lista_planos = ['basic', 'premium']
        if plano in self.lista_planos:
            self.plano = plano
        else:
            raise Exception('Plano inválido.')
        
    def mudar_plano(self, novo_plano):
        if novo_plano in self.lista_planos:
            self.plano = novo_plano
        else:
            raise Exception('Plano inválido.')

    def ver_filme(self, filme, plano_filme):
        if self.plano == plano_filme:
            print('Acesso permitido.')
        elif self.plano == 'premium' and plano_filme == 'basic':
            print('Acesso permitido')
        else:
            print('Acesso negado')


cliente1 = Cliente('Pedro', 'naosei@gmail.com', 'basic')
print(cliente1.plano)
cliente1.mudar_plano('premium')
print(cliente1.plano)
print()