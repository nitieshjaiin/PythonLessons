grade = int(input("Enter your Grade "))

if grade >= 90 and grade <= 100:
    print("Congratulations, you've scored Grade : A")
elif grade >= 80 and grade <= 89:
    print("Congratulations, you've scored Grade : B")
elif grade >= 70 and grade <= 79:
    print("Congratulations, you've scored Grade : C")
elif grade >= 60 and grade <= 69:
    print("Congratulations, you've scored Grade : D")
elif grade >= 50 and grade <= 59:
    print("Congratulations, you've scored Grade : F")
else:
    print("Invalid Score")
