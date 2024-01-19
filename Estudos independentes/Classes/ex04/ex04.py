
# Intermediário - Classe Funcionário: Crie uma classe chamada Funcionario com atributos para nome, cargo e salário. Adicione métodos para aumentar o salário e exibir as informações do funcionário.

import copy

class Employee():
    '''
    => Employee class with information about the employee
    '''
    
    def __init__(self, name, office, salary):
        '''
        => Create the class and add your information
        :param name: employer's name
        :param office: employee position
        :param salary: employee salary
        '''
        self.name = name
        self.office = office
        self.salary = salary

    def increase(self, value = 0):
        '''
        => Increase in employee salaries
        :param value: increase value
        '''
        self.salary += value

    def info(self):
        '''
        =>  View employee information
        '''
        print(f'\nName: {self.name}')
        print(f'Office: {self.office}')
        print(f'Salary: US${self.salary:.2f}')

list_of_employees = []

employee = Employee('Pedro', 'Teacher', 0.45)
list_of_employees.append(copy.deepcopy(employee))

employee = Employee('João Vitor', 'Programmer', 5000)
list_of_employees.append(copy.deepcopy(employee))

for person in list_of_employees:

    print('\n----------------------')
    person.info()
    person.increase(1500)
    person.info()

print('\n----------------------\n')