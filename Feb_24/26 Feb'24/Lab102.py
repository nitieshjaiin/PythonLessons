# Single inheritance

class Father:
    gold = 5

    def car(self):
        print("Audi")

    def home(self):
        print("This is father's home")

class Son(Father):
    pass

Nitish = Son()
Nitish.home()
Nitish.car()
print("You have gold of worth", Nitish.gold, "crore")