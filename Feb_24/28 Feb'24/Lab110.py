# Method overloading

# python doesn't support method overloading in traditional sense
# same name of a function with different Parameter

class MathUtil:
    def add(self, a,b=0, c=0):
        return a+b+c

math = MathUtil()
op = math.add(24)
op1 = math.add(24,33)
op2 = math.add(24,33,42)

