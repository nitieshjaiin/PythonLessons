"""Task - Calculate Factorial
# n = 5
# 5! -->5*4*3*2*1 -> 120
# 3! -> 3*2*1 -> 6
# 4! -> 4*3*2*1 -> 24"""

fact_num = int(input("Enter the number you wish to calculate factorial: "))
facto = 1
for i in range(1, fact_num + 1):
    facto = facto * i

print(f"The factorial of the number is: ", facto)
