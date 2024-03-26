class MyClass:
    def __init__(self):
        self.name = "Nitish"

    def public_func(self):
        print("Public Function")

    def __private_func(self):
        print("Private Function")

a = MyClass()
a.public_func()
print(a.name)