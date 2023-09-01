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
num = (input("Enter a number:"))
while num != str:
    print(f"number:{num}")
    num = int(input("Enter a number:"))
print ("stop")


#4
import random
guessesTaken = 0
number = random.randint(1,10)
print("I am thinking of a number bteween 1 and 10.")

while guessesTaken < 5:
    print("Take a guess.")
    guess = input()
    guess= int(guess)
    guessesTaken=guessesTaken+1
    if guess > number:
        print("Your guess is too high.")
    if guess < number:
        print("Your guess is too low.")
    if guess == number:
        print("You are right.")



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
