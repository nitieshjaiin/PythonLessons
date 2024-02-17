my_list = [2, 2, 3, 4, 5]


# map()
# map - map is a python building function

def sq_num(num):
    return num ** 2

# result = sq_num(4)
# print(result)

# map()- Takes each item from the list and execute the function on them.
# return same number of the elements (list in this case)

sq_numbers = list(map(sq_num,my_list))
print(sq_numbers)