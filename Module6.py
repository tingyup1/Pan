# 1
import random
def rollDice():
    return random.randint(1, 6)

result = rollDice()
print(f"roll number is: {result}")
while result != 6:
    result = rollDice()
    print(f"roll number is: {result}")


# 2
def rollDice(max):
    max=int(input("What is your maximum number on the dice:"))
    return max

result = rollDice(max)
while result != rollDice(max):
    result = rollDice(max)
    print(f"max roll number is:{result}")



# 3
import math
litre_pre_gallon = 3.78541178
def convert(litre, Gallon):
    return litre * litre_pre_gallon
volume =0
while volume >= 0:
    volume = int(input("enter a volume in gallons:"))
    print(volume * convert(1, 1))
print("stop")


#4
def sum_of_list(lst):
  total = 0
  for num in lst:
    total +=num
  return total

my_list = []
num=int(input("Do you want to add some number:"))
while num != int:
    num = int(input("Do you want to add some number:"))
    my_list.append(num)
    print(f"The sum of my_list is {sum_of_list(my_list)}")


#5




