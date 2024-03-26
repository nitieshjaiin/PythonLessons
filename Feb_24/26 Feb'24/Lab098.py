# Encapsulation - was used to bind the data variables and methods within class
# to hide the important variables

# Three different types of data variables -

# self.name = name is public
# _ is a protected variable
# __ is a private variable

class Car:
    public_name = None

    def __init__(self):
        self.public_name = "Public_name"
        self._protected_var = "Protected123"
        self.__private_var = "PRIVATE TEXT"
        print("Hello")

    def printName(self):
        print(self.public_name)


xuv = Car()
print(xuv.public_name)
