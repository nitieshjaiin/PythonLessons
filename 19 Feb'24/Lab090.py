class car:
    name = None
    color = None
    model = None
    speed = None
    engine = None

# self is a special character that is used in context of OOPs
# It is a reference to the instance of a class
# access and manipulate the attributes and methods of that instance

    def start_engine(self):
        print("Engine Started")

    def drive(self):
        print("Driving")

    def car_break(self):
        print("Break Applied", self.name)


tesla = car()
tesla.name = "Tesla"
tesla.car_break()