"""Task - Calculate Factorial
# n = 5
# 5! -->5*4*3*2*1 -> 120
# 3! -> 3*2*1 -> 6
# 4! -> 4*3*2*1 -> 24"""

fact_num = int(input("Enter the number you wish to calculate factorial: "))
facto = 1

while fact_num > 1:
    facto = fact_num * facto
    fact_num = fact_num - 1

print(f"The factorial of the number is: ", facto)