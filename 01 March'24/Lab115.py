# Handle Exception
# In Java, try and catch block
# In Python, try and except block
# Try executing the code in try and if any issues then execute the except code

a = int(input("Enter Number 1 \n"))
b = int(input("Enter Number 2 \n "))

try:
    c = a / b # Zero Dvision Error : division by zero
    print("Division is ", c)
except Exception as e:
    print(e)
    print("Print important message")

