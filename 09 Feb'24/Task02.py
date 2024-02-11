"""Write a program that classifies a triangle based on its side lengths.
Given three input values representing the lengths of the sides,
determine if the triangle is equilateral (all sides are equal),
isosceles (exactly two sides are equal), or scalene (no sides are equal)."""

side1 = float(input("Enter side1 of the triangle: "))
side2 = float(input("Enter side2 of the triangle: "))
side3 = float(input("Enter side3 of the triangle: "))

if side1 == side2 == side3:
    print("The triangle is an equilateral triangle.")
elif side1 == side2 or side2 == side3 or side1 == side3:
    print("The triangle is an isosceles triangle")
else:
    print("The triangle is a scalene triangle")