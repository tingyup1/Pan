#1
import random
numDices=int(input("How many dice to roll:"))
result = 0

for i in range(numDices):
    rollDice = random.randint(1,6)
    result+=rollDice
print(result)



#2
list=[]
while True:
    num = input("Enter a number you want to add,if want to quit,enter empty string:")
    list.append(num)
    print(list)
    if num == '':
        list.remove(list[-1])
        break

list.sort(reverse = True)
print(list)



#3

number=int(input("Enter a integer number:"))
for i in range(number):
    if number%1==0 and number%number==0:
        print("Prime number")
    else:
        print("Not a prime number.")

#4
citiesInput = str(input("Enter five city name:"))
cities = citiesInput.split(',')  # delimiter: comma, returns an array
for city in cities:
    print(city)
