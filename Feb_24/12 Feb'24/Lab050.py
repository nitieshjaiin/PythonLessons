# Match case

numbers = int(input("Enter a number \n"))

match numbers:
    case 1:
        print("Your input is number 1")
    case 2:
        print("Your input is number 2")
    case 3:
        print("Your input is number 3")
    case 4:
        print("Your input is number 4")
    case 5:
        print("Your input is number 5")
    case _:
        print("Your input is unknown")