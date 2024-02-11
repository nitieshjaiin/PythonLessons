"""Task
#Fibonaci series - 0,0+1, 0+1+1,
# n = 7, then 0, 1, 1,  2, 3, 5, 8, 13"""
fibo_range = int(input("Enter the range of fibonacci series: "))
num1 = 0
num2 = 1
print("Your fibonacci series is as below: \n")
print(num1, end=" ")
print(num2, end=" ")
for i in range(1, fibo_range):
    num3 = num1 + num2
    print(num3, end=" ")
    num1 = num2
    num2 = num3
