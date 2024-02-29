# hybrid inheritance
class A:
    def method_A(self):
        return "Method A"

class B(A):
    def method_B(self):
        return "Method B"

class C(A):
    def method_C(self):
        return "Method C"

class D(B,C):
    def method_D(self):
        return "Method D"


d = D()
print(d.method_A())
print(d.method_D())
print(d.method_B())
print(d.method_B())