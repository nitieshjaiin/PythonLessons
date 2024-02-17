import math



def sq_root(num):
    return math.sqrt(num)

my_list = [24, 33, 42]

sq_list = list(map(sq_root,my_list))
print(sq_list)
