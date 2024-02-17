# *args and **kargs

# * args - to pass any number of arugments

def sum_num(a,b,c):
    return a+b+c


r = sum_num(2,3,4)
print(r)

sm = sum_num(a=2,b=6,c=7)
print(sm)

def print_arg (*args):
    for i in args:
        print(i, end=" ")


print_arg(1,2,3,4,5,6)