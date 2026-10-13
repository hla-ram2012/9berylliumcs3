class Bank_Account:
    def __init__(self, account_number: int, balance: float):
        self.__account_number = account_number
        self.__balance = balance

    def account_number(self):
        return self.__account_number

    #@account_number.setter
    def set_account_number(self, account_number):
        self.__account_number = int(input("Set account number to "))
        return self.__account_number
    
    #@balance.setter
    def set_balance(self):
        balance_initial = float(input("Update balance to "))
        if balance_initial >= 0:
            self.__balance = balance_initial
            return self.__balance
        else:
            return print("The balance must not be a negative number.")
    
    #@account_number.getter
    def get_account_number(self):
        return f'Account Number: {self.__account_number}'
    
    #@balance.getter
    def get_balance(self):
        return f'Balance: {self.__balance}'
    
    #@property
    def account_number(self):
        return self.__account_number

    #@property
    def balance(self):
        return self.__balance

a1 = Bank_Account(12345, 1000.0)
print(a1.get_account_number())
print(a1.get_balance())
print()
a1.set_balance()
print(a1.get_account_number())
print(a1.get_balance())
