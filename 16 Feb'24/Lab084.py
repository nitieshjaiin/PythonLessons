my_dict = {'c': 2, 'a': 4, 'b': 6}

for k,v in my_dict.items():
    if k == 'b':
        print("B is found")


op = 'b' in my_dict
print(op)
