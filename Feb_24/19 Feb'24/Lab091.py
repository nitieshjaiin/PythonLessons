class Cal:
    def sum(self,a,b):
        return a+b

    def multiply(self,a,b):
        return a * b

    def sub(self,a,b):
        return a - b


ob = Cal()
result = ob.sum(20,4)
print(result)
print(ob.sub(28,4))
print(ob.multiply(6,4))