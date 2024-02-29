# Abstraction - OOPs
# Hiding the details and showing only what is required
# i.e. hide the implementation and show only the important details
# Abstract base classes
# Abstract base methods

from abc import ABC, abstractmethod
class Animal(ABC):
    def __init__(self,name):
        self.name = name

    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Bow Bow"

class Cat(Animal):
    def sound(self):
        return "MEOW"

dog = Dog("Pluto")
print(dog.sound())
cat = Cat("Billo")
print(cat.sound())