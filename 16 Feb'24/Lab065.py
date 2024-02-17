# filter

# it can filter the items from the list based on the logi and return less number of items


my_list = [1,2,4,1,8,2,5,6,63,4,1,2,5,78,345,2,24,4,65,32,423]

even_num = filter(lambda x: x % 2 == 0,my_list)
print(list(even_num))

