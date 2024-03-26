from abc import ABC, abstractmethod

class ATB(ABC):
    def __init__(self,name):
        self.name = name

    @abstractmethod
    def perform_task1(self):
        pass
    @abstractmethod
    def perform_task2(self):
        pass

class Nitish(ATB):
    def perform_task1(self):
        return "Task1"

    def perform_task2(self):
        return "Task2"

nitish = Nitish("A")
print(nitish.perform_task1())
print(nitish.perform_task2())