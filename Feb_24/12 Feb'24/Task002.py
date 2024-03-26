# Create a function to calculate the factorial of a number.
def fact(num):
    facto = 1
    while num > 1:
        facto = num * facto
        num = num - 1
    return facto


fact_num = int(input("Enter the number you wish to calculate factorial: "))
factor = fact(fact_num)
print(f"The factorial of the entered number is: ", factor)

