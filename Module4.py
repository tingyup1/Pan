#1
import math
number = int(input("Enter a number:"))
number = 1
while  number <= 1000:
    if not number%3:
      print(number)
    number = number + 1

#2converts inches to centimeters until the user inputs a negative value
import math
inch_value = int(input("Enter a value:"))
cm_value = 2.54*inch_value
inch_value = 1
while (inch_value>=1):
    print(f"{inch_value}={cm_value}")
    inch_value = inch_value + 1
    if inch_value <=-1:
        break



#3
list=[]
num = input("enter a number,if want to quit,enter empty str:")
while num != '':
    num=input("enter a number,if want to quit,enter empty str:")
    list.append(num)
    print(max(list),min(list))


#4
import random
num=random.randint(1,10)
guessNum=int(input("Enter a number(1-10):"))
while True:
    if guessNum<num:
        print(f"random num is {num},Too low")
    break

while True:
    if guessNum>num:
      print(f"random num is {num},Too high")
    break

while True:
    if guessNum==num:
      print(f"random num is {num},Correct")
    break


#5
print("Enter correct username and password")
count = 0
while count < 5:
    username = input("Enter your username:")
    password = input("Enter your password:")
    if password == "12345" and username == "MYNAME":
        print("Welcome!")
        break
    else:
        print("Access denied.")
        count=count+1

#6
