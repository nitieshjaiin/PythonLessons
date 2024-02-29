# single inheritance - 80% this will be used
# multiple inheritance
# multi-level inheritance
# hybrid inheritance


# Hierarchical inheritance

class Vehicle:
    def Info(self):
        print("This is a vehicle class")

class Car(Vehicle):
    def Info(self):
        print("This is a car class")

class Bicycle(Vehicle):
    def Info(self):
        print("This is a Bicycle class")


car = Car()
bicycle = Bicycle()

car.Info()
bicycle.Info()