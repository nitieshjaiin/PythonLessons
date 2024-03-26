
class XYZ:
    def f1(self):
        try:
            a = int(input("Enter Number 1"))
        except Exception as e:
            print("Enter integer value only")
        else:
            print(a)
        finally:
            print("Mandatory excepted")

x = XYZ()
x.f1()