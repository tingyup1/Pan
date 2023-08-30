import math
pi = 3.1415926
formatPI = ("value of PI: {:.2f}".format(math.pi))
radius = float(input("Enter the radius:"))
areaCircle = math.pi * radius ** 2
print(f"Area of the circle:{areaCircle:.2f} ")
