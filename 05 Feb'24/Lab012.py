# Take inputs from end user and add them.

num1 = input("Enter the First Number")

num2 = input("Enter the Second Number")

print(num1)
print(num2)
print(type(num1))

num3 = num2 + num1  #It will concatenate unless we convert them into integer
print(num3)

num3 = int(num1) + int(num2) #Converting string to integer
print("Integer Sum is ", num3)


