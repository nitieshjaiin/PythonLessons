# Classes & Objects in Python
# Class - contains Attributes & Behaviour

# If person is a class, then objects are like Nitish, Adarsh, Jyotsna etc

class Person:
    # Attributes, also called as data members
    name = None
    age = None
    ID = None
    phone_no = None

    # behaviour also called as methods

    def talk(self):
        print("Talking")

    def sleep(self):
        print("Sleeping")

    def walk(self):
        print("Walking")

# Object creation -> ClassName()
nitish = Person()
nitish.name = "Nitiesh"
print(nitish.name)
nitish.sleep()
nitish.walk()
