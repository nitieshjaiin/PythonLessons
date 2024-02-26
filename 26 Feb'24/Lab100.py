class Bank_Acc:
    def __init__(self):
        self.balance = 0
        self.__private_var = 100

    def deposit(self, amount):
        self.balance += amount

    def _withdraw(self,amount):
        self.balance -= amount

    def __show_balance(self):
        print("Your account balance is ", self.balance)

    def if_access(self,flag):
        if flag:
            self.__show_balance()
        else:
            print("Not allowed")

    def bank_manager(self, amount):
        self._withdraw(amount = amount)

city = Bank_Acc()
city.deposit(1000)
city.bank_manager(699)
city.if_access(True)
city.if_access(False)