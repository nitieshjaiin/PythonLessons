class Car:
    name = None
    make = None
    Model = None

    def __init__(self, o_name, o_make, o_model): # Constructor
        self.name = o_name
        self.make = o_make
        self.Model = o_model

    def start_engine(self):
        print("Starting a car with name " + self.name)
        print("Starting a car with make " + self.make)
        print("Starting a car with Model " + self.Model)


lambo = Car("lambo", "V2", "2024")
lambo.start_engine()
audi = Car("Audi","V24","'24")
audi.start_engine()
print(id(lambo))
print(id(audi))