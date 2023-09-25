# defining BankAccount class

class BankAccount:
    def __init__(self,amount):
        self.__balance = amount

    def deposit(self,amount):
        self.__balance += amount

    def withdraw(self,amount):
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            print('Insufficient balance')

    def get_balance(self):
        return self.__balance


# Create BankAccount object and perform operations

amount = int(input('Enter the initial amount to open your account: ')) 
account = BankAccount(amount)
print('Your balance is', account.get_balance())

amount = int(input('Enter amount to deposit: '))
account.deposit(amount)
print('Your balance is', account.get_balance())

amount = int(input('Enter amount to withdraw: '))
account.withdraw(amount)
print('Your balance is', account.get_balance())
