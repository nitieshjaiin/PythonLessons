"""
Create a program that takes two numbers as input and prints whether the first number
is greater than, less than, or equal to the second number.
"""

first_num = input("Enter first number: ")
sec_num = input("Enter second number: ")

grt = (first_num > sec_num)
sec_grt = (first_num < sec_num)
eq = (first_num == sec_num)

print(f"Number one is greater than 2 ", grt)
print(f"Number 2 is greater than one ", sec_grt)
print(f"Both number one and number 2 are equal", eq)