# try, except and finally
# multiple exceptions

try:
    a = int(input("Enter Number 1 \n"))
    b = int(input("Enter Number 2 \n "))
    c = a / b
except ValueError as v:
    print(v)
except ZeroDivisionError as z:
    print(z)
else:
    print(f"Result is {c}")
finally:
    print("I'll be always executed")
