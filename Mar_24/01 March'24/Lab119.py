class MyCustomException(Exception):
    def __init__(self, msg):
        self.message = msg
        super().__init__(self.message)


bal = 100
withdraw_am = int(input("Enter the amount you want to withdraw"))

if withdraw_am > bal:
    raise MyCustomException("Your Balance is Low!")
else:
    print("Total after withdrawal is ", bal - withdraw_am)
