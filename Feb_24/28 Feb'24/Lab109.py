# Method overriding - same name in the parent and child

class Animal:
    def __init__(self):
        pass
    def sound(self):
        print("Animal Sound")

class Dog(Animal):
    def __init__(self):
        pass
    def sound(self):
        super().sound() # this is used to call the super functional of the inherited class
        print("Dog Sound")

# super - just calls the parent class function


animal = Animal()
animal.sound()

dog = Dog()
dog.sound()