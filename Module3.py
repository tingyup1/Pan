#1
import math
length = int(input("What the length of a zander in centimeters?"))
x = int(42-length)
if length < 42:
    print(f"Please release the fish back into the lake. There have {x} centimeters below the size limit")
else:
    print("You can catch it")


#2
cabin = str(input("Please enter the cabin class of a cruise ship:"))

if (cabin == "LUX"):
    print("upper-deck cabin with a balcony")
elif (cabin == "A"):
    print("above the car deck, equipped with a window")
elif(cabin == "B"):
    print("windowless cabin above the car deck")
else:
    print(" windowless cabin below the car deck")


