set1 = {1,2,3,4,5}
set2 = {5,6,7,8,2,1}

my_set = set1.union(set2) # joins the sets but removes the duplicates
print(my_set)

my_set2 = set1.intersection(set2) # provides the common between 2 sets
print(my_set2)

my_set3 = set1.difference(set2) # provides the unique items in first set by comparing in set2
print(my_set3)

my_set4 = set2.difference(set1) # returns the unique items in set2 in comparison to set1
print(my_set4)