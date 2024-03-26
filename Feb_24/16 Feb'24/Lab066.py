# Tuples - collection of items like list but we cant mutate them

# lists are mutable as below
my_list = [1,2,3,4,5,3,1]
my_list[0] = 0
print(my_list)

# tuple
my_tuple = (1,2,3,4,5)
#my_tuple[0] = 0 you can't mutate the list
print(my_tuple)
print(type(my_tuple))
print(len(my_tuple))
print(type(my_list))

new_tup = tuple(my_list)
print(new_tup)
print(type(new_tup))