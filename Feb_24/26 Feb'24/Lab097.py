# Encapsulation
# Data Variables/ Class Variables
# Functions - they are closed within a single blueprint/class
# Wrapping or binding the data variables with the methods

class Car:
    name = None

    def __init__(self,name):
        self.name = name

    def printName(self):
        print(self.name)


xuv = Car("xuv")
xuv.printName()
audi = Car("Audi")
audi.printName()