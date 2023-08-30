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
elif(cabin == "C"):
    print("windowless cabin below the car deck")
else:
    print("Invalid cabin class")


#3
import math
gender = str(input("Please enter your biological gender:"))
hemoglobin = int(input("Please enter your hemoglobin value (g/l):"))
if (117 <= hemoglobin <= 155 and gender == "females"):
    print("The hemoglobin value is normal.")
elif(hemoglobin < 117 and gender == "females"):
    print("The hemoglobin value is low.")
elif(hemoglobin > 155 and gender == "females"):
    print("The hemoglobin value is high.")
if(134 <= hemoglobin <= 167 and gender == "males"):
    print("The hemoglobin value is normal.")
elif(hemoglobin < 134 and gender == "males"):
    print("The hemoglobin value is low.")
elif(hemoglobin > 167 and gender == "males"):
    print("The hemoglobin value is high.")


#4
year = int(input("Enter a year:"))
if(year/4==0 or year/400==0):
    print("That is a leap year.")
else:
    print("That is not a leap year.")
