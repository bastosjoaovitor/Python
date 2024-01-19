
# Intermediário - Classe Conta Bancária: Crie uma classe chamada ContaBancaria com atributos para o titular da conta e saldo. Adicione métodos para depósito, saque e exibição do saldo.

import sqlite3
import pickle
from time import sleep
# makes the necessary imports into the program


def typing_effect(msg, interval = 0.05):
    '''
    => Typing effect.
    :param msg: Message that will be displayed.
    :param interval: Time interval for each letter to appear on the screen.
    '''
    from time import sleep
    for caractere in msg:
        print(caractere, end='', flush=True)
        sleep(float(interval))


def read_value(msg, type = str, limited_options= False, options = 0, remove_spaces = False):
    '''
    => Receives input and handles errors.
    :param msg: message that will be shown when requesting entry.
    :param type: input value type.
    :param limited_options: Limited entry options.
    :param options: Available options.
    :param remove_spaces: removes extra spaces on the left and right sides of the input.
    '''

    while True:

        try:
            value = input(msg)
            if value == '':
                print('\n\033[31mInvalid Input\033[m')
                continue
            if remove_spaces == True:
                value = value.strip()
            if type == int:
                value = int(value)
            elif type == float:
                value = float(value)
            if limited_options == True:
                if value in options:
                    break
                else:
                    print('\n\033[31mInvalid Input\033[m')
                    continue
            break
        except:
            print('\n\033[31mInvalid Input\033[m')
    return value


class Bank_Account():
    '''
    => Bank account class, stores user and password information, and stores deposit and withdrawal functions.
    '''

    def __init__(self, name, cpf, date_of_birth, balance, password):
        '''
        => Class constructor method.
        :param name: username
        :param cpf: user cpf
        :param date_of_birth: user's date of birth
        :param balance: user money
        :param password: user password
        '''
        self.name = name
        self.cpf = cpf
        self.date_of_birth = date_of_birth
        self.balance = balance
        self.password = password

    def deposit(self, value):
        '''
        => Deposits user money into the bank.
        :param value: amount that will be deposited
        '''
        self.balance += value

    def withdraw(self, value):
        '''
        => Gives user money.
        :param value: amount that will be withdrawn
        '''
        if value <= self.balance:
            self.balance -= value
            typing_effect(f'\n\033[32mUS${withdraw:.2f} SUCCESSFULLY WITHDRAWN\033[m\n')
            return value
        else:
            typing_effect('\n\033[31mInsufficient funds.\033[m\n')
# class to manage the user and his bank account


database_path = 'Python/Estudos independentes/Classes/ex03/database-bank-account-ex03.db'
connection = sqlite3.connect(database_path)
cursor = connection.cursor()
# connect to the database and create the cursor so you can interact with it


cursor.execute('''CREATE TABLE IF NOT EXISTS registro (id INTEGER PRIMARY KEY, name TEXT, cpf TEXT, date_of_birth TEXT, balance REAL, password TEXT, serialized_object BLOB)''')
# create the records table


while True:

    print()
    print(40*"=")
    print(f'{"\033[4mBank Account\033[m":^47}') # + 7
    print(40*"=")
    # title

    print('''
[ 1 ] - Login
[ 2 ] - Register
[ 3 ] - Finish''')
    # available options
    

    option_1 = read_value('\nOpção: ', int, True, [1,2,3], True)
    # user choice


    if option_1 == 1:
    # login
        
        while True:
            cpf = str(read_value('\nEnter your cpf (only numbers): ', int, remove_spaces=True))
            if len(cpf) != 11:
                print('\n\033[31mThe CPF has 11 digits\033[m')
                continue
            cpf = cpf[:3] + '.' + cpf[3:6] + '.' + cpf[6:9] + '-' + cpf[9:]
            break
        # read the cpf

        password = read_value('\nPassword: ')
        # read the password

        cursor.execute('SELECT (cpf) FROM registro ORDER BY id')
        # extract cpfs from database

        cpfs_tuple = cursor.fetchall()
        # saves the extracted cpfs

        list_of_cpfs = [item[0] for item in cpfs_tuple]
        # create a list with cpfs

        cursor.execute('SELECT (password) FROM registro ORDER BY id')
        # extract passwords from database

        tuple_of_passwords = cursor.fetchall()
        # saves the extracted passwords

        password_list = [item[0] for item in tuple_of_passwords]
        # create a list of passwords

        try: 
            if list_of_cpfs.index(cpf) == password_list.index(password):
                access = True
            else:
                access = False
        except:
            access = False
        # Confirms that the user's CPF and password are correct and compatible and denies or allows account based on that

        if access == False:
            typing_effect('\n\033[31mACCESS DENIED, TRY AGAIN\033[m\n')
        # informs the user that access has been denied and returns to the menu
        else:

            typing_effect('\n\033[32mACCESS ALLOWED\033[m\n')
            # informs the user that access has been granted

            while True:

                typing_effect('''
[ 1 ] - My bank account
[ 2 ] - Deposit
[ 3 ] - Withdraw
[ 4 ] - Log out\n''', 0.02)
# options in the user's bank account

                option_2 = read_value('\nOpção: ', int, True, [1,2,3,4], True)
                # user choice


                if option_2 == 1:
                # user information

                    cursor.execute(f'SELECT serialized_object FROM registro WHERE id = {password_list.index(password) + 1}')
                    user = cursor.fetchone()[0]
                    user = pickle.loads(user)
                    # pulls the user object stored in the database

                    typing_effect(f'''
Information about your bank account:

● Name: {user.name}
● Cpf: {user.cpf}
● Date of birth: {user.date_of_birth}
● Balance: US${user.balance:.2f}
● Password: {user.password}\n''', 0.02)
# available options


                elif option_2 == 2:
                # deposit

                    deposit = read_value('\nAmount to be deposited: US$', int)
                    user.deposit(deposit)
                    typing_effect(f'\n\033[32mUS${deposit:.2f} SUCCESSFULLY DEPOSITED\033[m\n')


                elif option_2 == 3:
                # withdraw

                    withdraw = read_value('\nAmount to be withdraw: US$', int)
                    user.withdraw(withdraw)


                elif option_2 == 4:
                # back to menu
                    break

                serialized_user = pickle.dumps(user)
                cursor.execute("UPDATE registro SET serialized_object = ? WHERE cpf = ?", (serialized_user, user.cpf))
                connection.commit()


    elif option_1 == 2:
    # register

        name = read_value('\nType your name: ')
        # read the name

        while True:
            cpf = str(read_value('\nEnter your cpf (only numbers): ', int, remove_spaces=True))
            if len(cpf) != 11:
                print('\n\033[31mThe CPF has 11 digits\033[m')
                continue
            cpf = cpf[:3] + '.' + cpf[3:6] + '.' + cpf[6:9] + '-' + cpf[9:]
            break
        # read the cpf

        while True:
            date_of_birth = str(read_value('\nEnter your birth date (only numbers): ', int, remove_spaces=True))
            if len(date_of_birth) != 8:
                print('\n\033[31mThe date of birth has 8 digits\033[m')
                continue
            date_of_birth = date_of_birth[:2] + '/' + date_of_birth[2:4] + '/' + date_of_birth[4:]
            break
        # read the date of birth

        balance = read_value('\nEnter your balance: ', float)
        # read the balance

        password = read_value('\nPassword: ')
        # read the password

        user = Bank_Account(name, cpf, date_of_birth, balance, password)
        # create a bank account

        serialized_user = pickle.dumps(user)
        # serialize the object to be compatible with the database

        cursor.execute("INSERT INTO registro (name, cpf, date_of_birth, balance, password, serialized_object) VALUES (?, ?, ?, ?, ?, ?)", (user.name, user.cpf, user.date_of_birth, user.balance, user.password, serialized_user))
        # stores the data in the database

        connection.commit()
        # save edits

        typing_effect('\n\033[32mACCOUNT REGISTERED SUCCESSFULLY\033[m\n')
        sleep(1)
        # message displayed after account registration


    elif option_1 == 3:
    # finish
        
        typing_effect('\nFinishing program')
        typing_effect('...', 1)
        typing_effect('\n\nGoodbye\n\n', 0.01)
        break
        # end of program

connection.commit()
# saves changes made to the database
connection.close()
# closes the connection to the database