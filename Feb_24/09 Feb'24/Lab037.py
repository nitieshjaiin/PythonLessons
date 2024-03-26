# Find the maximum between 3 numbers

num1 = int(input("Enter Number 1"))
num2 = int(input("Enter Number 2"))
num3 = int(input("Enter Number 3"))

# max_num = max(num1,num2,num3)
# print(max_num)

if num1 > num2 and num1 > num3:
    print("Maximum number is number 1")
elif num2 > num1 and num2 > num3:
    print("Maximum number is number 2")
else:
    print("Maximum number is number 3")