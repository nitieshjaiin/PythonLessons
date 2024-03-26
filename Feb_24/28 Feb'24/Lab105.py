# Multiple inheritance

class Father:
    def home(self):
        print("This is father's function")


class Mother:
    def home(self):
        print("this is mother's function")


class Son(Father, Mother):
    pass
    # def home(self):
    #     print("This is son's function")


son = Son()
son.home()  # the function will be called basis who is inherited first, basis MRO - Method Resolution Order
print(Son.mro())  # to identify the order of method resolution
