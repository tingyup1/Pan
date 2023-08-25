#Write a program that asks your name and then greets you by your name
user = input("Enter your name:\n")
print("Hello,"+ user +"!")


#Write a program that asks the user for the radius of a circle and the prints out the area of the circle
import math
pi = 3.1415926
formatPI = ("value of PI: {:.2f}".format(math.pi))
radius = float (input("Enter the radius:"))
areaCircle = math.pi * radius **2
print(f"Area of the circle:{areaCircle:.2f} ")

#Caculate the length and width of rectangle
import math
length = int (input("Enter the lenth of the rectangle:"))
width = int (input("Enter the width of the rectangle:"))
perimeter = (length + width) * 2
print(f"perimeter of the rectangle: {perimeter}")
area = length * width
print(f"Area of the rectangle: {area}")

#Caculate sum,product and average of three integer
print("Please enter three integer numbers.")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
sumNumber =int (num1 + num2 + num3)
productNumber = int (num1 * num2 * num3)
averageNumber = int ((num1 + num2 + num3)/3)
print(f"sum:{sumNumber}")
print(f"product:{productNumber}")
print(f"average:{averageNumber}")


#Changing units
import math
ONE_TALENT_TO_POUND = 20
ONE_POUND_TO_LOT = 32
ONE_LOT_TO_GRAM = 13.3
ON_KILOGRAM_TO_GRAM=1000
talent = float(input("Enter talents:"))
pound = float(input("Enter pounds:"))
lot = float(input("Enter lots:"))

talentsTOGram  = (ONE_TALENT_TO_POUND * ONE_POUND_TO_LOT * ONE_LOT_TO_GRAM)
poundsTOGram  = (ONE_POUND_TO_LOT * ONE_LOT_TO_GRAM)
lotsTOGram  = (ONE_LOT_TO_GRAM)

talentsTOKilogram  = (talentsTOGram/1000)
poundsTOKilogram = (poundsTOGram/1000)
lotsTOKilogram  = (lotsTOGram/1000)

print("The weight in modern units:")
print(talentsTOKilogram,"kilograms\t and" ,talentsTOGram,"grams.")
print(poundsTOKilogram,"kilograms\t and" ,poundsTOGram ,"grams.")
print(lotsTOKilogram,"kilograms\t and" ,lotsTOGram,"grams.")


#combination


