# lambda expression - to help covert the function in one-liner


def double_salary(salary):
    return salary * 2

result = double_salary(200000)
print(result)


double_salary2 = lambda salary2: salary2*2
print(double_salary2(100))

sm = lambda a,b : a+b
print(sm(3,3))