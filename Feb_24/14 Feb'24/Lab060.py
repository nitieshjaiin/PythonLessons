# list - collection of items and duplicates are allowed

my_list = [1,2,"Nitish", 23, 42]

print(my_list[0])

# changing an element

my_list[0] = 10
print(my_list)

# append a list

my_list.append(33)
print(my_list)

# extend a list
my_list.extend([24,6])
print((my_list ))

# insert
my_list.insert( 0,'a')
print(f"List after inserting is ", my_list)

# remove
my_list.remove('a')
print(f"List after removing a is ", my_list)

# copy list

new_list = my_list.copy()
print("New list is ", new_list)

# clear list
my_list.clear()
print("Cleared list is ", my_list)
print(new_list)

# finding index of value in list
print(f"The index of 24 in list is ", new_list.index(24))

# sorting list
# new_list.sort()
# print(new_list) #will work on same data type, sorting is not allowed on heterogeneous data

# reverse list

print("The reverse list is ", new_list.reverse())

# check if list is empty
if not new_list:
    print("List is empty")
else:
    print("List has data")