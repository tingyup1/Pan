#1
import random
print("how many dice do you roll?")
dice = [1,2,3,4,5,6]
dice = input("roll the dice:")
while dice !=dice:
    dice = input("How many dice to roll?")

for n in dice:
    print(f"sum is:{n}")

#2
input_List = []
input_List.append(int(input("Enter a number:")))
while True:
    a=input("Do you want to input more:")
    if a == "yes" or a=="YES":
        input_List.append(int(input("Enter a number:")))
    elif a== "":
        input_List.sort(reverse=True)
        break
print(input_List)


#3