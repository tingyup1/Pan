# 1
import random
def rollDice():
    roll=random.randint(1,6)
    return roll
result=rollDice()
while result!=6:
    result = rollDice()
    print(f"the result is {result}")


# 2
def rollDice(max):
    max=int(input("What is your maximum number on the dice:"))
    return max

result = rollDice(max)
while result != rollDice(max):
    result = rollDice(max)
    print(f"max roll number is:{result}")



# 3
def conversionn():
    liter_per_gallon=3.78
    liters=gallon*liter_per_gallon
    print(f"Gallon converts to litrer is {liters}")

gallon=int(input("Enter number of gallon you want to convert:"))
while gallon>=0:
    conversionn()
    gallon = int(input("Enter number of gallon you want to convert:"))
print("not valid")


#4
def sum_of_list(list):
    sum=0
    for num in list:
        sum+=num
    return sum
list=[1,2,3,4,5,6,7,8]
print(sum_of_list(list))


#5
def uneven_list(list):
    for num in list:
        num % 2 != 0
        list = list.remove(num)
    print(list)


list = [1, 2, 3, 4, 5, 6, 7, 8]
uneven_list(list)


#6
import math
def cost_of_pizza():
    diameter=int(input("enter the diameter of pizza:"))
    pizzaCost=int(input("enter the cost of pizza:"))
    areaPizza= math.pi * (diameter/2) ** 2
    unit_cost_of_Pizza=pizzaCost/areaPizza
    return unit_cost_of_Pizza

Pizza1= cost_of_pizza()
Pizza2= cost_of_pizza()
if Pizza1 > Pizza2:

    print("You can choose pizza1")
else:
    print("You can choose pizza2")
