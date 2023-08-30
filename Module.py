# 1
user = input("Enter your name:\n")
print("Hello," + user + "!")

#2
import math
pi = 3.1415926
formatPI = ("value of PI: {:.2f}".format(math.pi))
radius = float(input("Enter the radius:"))
areaCircle = math.pi * radius ** 2
print(f"Area of the circle:{areaCircle:.2f} ")

#3
import math
length = int(input("Enter the lenth of the rectangle:"))
width = int(input("Enter the width of the rectangle:"))
perimeter = (length + width) * 2
print(f"perimeter of the rectangle: {perimeter}")
area = length * width
print(f"Area of the rectangle: {area}")

#4
import math
print("Please enter three integer numbers.")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
sumNumber = int(num1 + num2 + num3)
productNumber = int(num1 * num2 * num3)
averageNumber = int((num1 + num2 + num3) / 3)
print(f"sum:{sumNumber}")
print(f"product:{productNumber}")
print(f"average:{averageNumber}")

#5
import math
ONE_TALENT_TO_POUND = 20
ONE_POUND_TO_LOT = 32
ONE_LOT_TO_GRAM = 13.3
ONE_KILOGRAM_TO_GRAM = 1000
talent = float(input("Enter talents:"))
pound = float(input("Enter pounds:"))
lot = float(input("Enter lots:"))

talentsTOGram = ONE_TALENT_TO_POUND * ONE_POUND_TO_LOT * ONE_LOT_TO_GRAM * talent
poundsTOGram = ONE_POUND_TO_LOT * ONE_LOT_TO_GRAM * pound
lotsTOGram = ONE_LOT_TO_GRAM * lot

talentsTOKilogram = (talentsTOGram / 1000)
poundsTOKilogram = (poundsTOGram / 1000)
lotsTOKilogram = (lotsTOGram / 1000)
totalWeightInKilos = talentsTOKilogram + poundsTOKilogram + lotsTOKilogram
weightKiloPart = int(totalWeightInKilos)
weightGramPart = format((totalWeightInKilos-int(totalWeightInKilos))*1000, ".2f")
print("The weight in modern units:")
print(str(weightKiloPart) + " kilograms and " + str(weightGramPart) + " grams.")


#6
import random
a = random.randint(0, 9)
b = random.randint(0, 9)
c = random.randint(0, 9)
print("Combination:" + str(a) + str(b) + str(c))

a = random.randint(1, 6)
b = random.randint(1, 6)
c = random.randint(1, 6)
d = random.randint(1, 6)
print("Combination:" + str(a) + str(b) + str(c) + str(d))










