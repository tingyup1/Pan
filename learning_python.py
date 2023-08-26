# Write a program that asks your name and then greets you by your name
user = input("Enter your name:\n")
print("Hello," + user + "!")

# Write a program that asks the user for the radius of a circle and the prints out the area of the circle
import math

pi = 3.1415926
formatPI = ("value of PI: {:.2f}".format(math.pi))
radius = float(input("Enter the radius:"))
areaCircle = math.pi * radius ** 2
print(f"Area of the circle:{areaCircle:.2f} ")








