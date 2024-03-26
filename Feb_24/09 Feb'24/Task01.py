"""Create a program that determines whether a given year is a leap year.
A leap year is divisible by 4, but not by 100 unless it is also divisible by 400.
Use an if-else statement to make this determination."""

year = int(input("Enter the year you wish to find as leap year"))

if year % 4 == 0 and year % 100 != 0:
    print("Your input year is a loop year")
elif year % 100 == 0 and year % 400 == 0:
    print("Your input year is a leap year")
else:
    print("Your input isn't a loop year")
