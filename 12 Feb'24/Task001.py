# Create a function to check if the user input is palindrome or not
def palindrome(value):
    input_len = len(value)
    reverse_input = ''
    counter = -1
    for i in range(1, input_len + 1):
        reverse_input = str(reverse_input) + value[counter]
        counter = counter - 1
    if value == reverse_input:
        return "Your input value is palindrome"
    else:
        return "Your input value isn't palindrome"


user_input = input("Enter the palindrome you want to check: ")
check = palindrome(user_input)
print(check)
