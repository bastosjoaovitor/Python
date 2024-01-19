
# Avançado - Classe Agenda: Crie uma classe chamada Compromisso com atributos para descrição, data e hora. Em seguida, crie uma classe Agenda que contém uma lista de objetos Compromisso. Adicione métodos para agendar, cancelar e exibir compromissos.

class Commitment():

    def __init__(self, description, date, hour):

        self.description = description
        self.date = date
        self.hour = hour

class Schedule():

    def __init__(self):

        self.schedule = []

    def add_commitment(self, commitment):

        if isinstance(commitment, Commitment):
            self.schedule.append(commitment)

    def del_commitment(self, commitment):

        if commitment in self.schedule:
            self.schedule.remove(commitment)

    def show_commitment(self, commitment):
        if commitment in self.schedule:
            print(commitment)

    def show_schedule(self):
        for element in self.schedule:
            print(element.description)

compromisso_1 = Commitment('Fazer uma prova', '22/22/2222', 15)
compromisso_2 = Commitment('Correr', 'amanha', 6)

agenda = Schedule()

agenda.add_commitment(compromisso_1)
agenda.add_commitment(compromisso_2)

print(agenda.show_schedule)


