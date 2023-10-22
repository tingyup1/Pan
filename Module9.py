#1
class Car:

    def __init__(self,registration_num,maxi_speed,current_speed=0,travel_distance=0):
        self.registration_num=registration_num
        self.maxi_speed=maxi_speed
        self.current_speed=current_speed
        self.travel_distance=travel_distance

c1=Car('ABC-123',142)
print(f'Registration number:{c1.registration_num}\n Maximum speed:{c1.maxi_speed}km/h'
      f'\n current speed and travelled distance:{c1.current_speed}and{c1.travel_distance}')


#2
class Car:

    def __init__(self,registration_num,maxi_speed,current_speed=0,travel_distance=0):
        self.registration_num=registration_num
        self.maxi_speed=maxi_speed
        self.current_speed=current_speed
        self.travel_distance=travel_distance

    def accelerate(self,delta_speed):
        self.current_speed+=delta_speed
        if self.current_speed > self.maxi_speed:
            self.current_speed=self.maxi_speed
        elif self.current_speed < 0 :
            self.current_speed=0

    def emergency_brake(self,es):
        if es==(-200):
            self.current_speed = 0
            print("Emergency brake!")

c1=Car('ABC-123',142)
c1.accelerate(30)
c1.accelerate(70)
c1.accelerate(50)
print(f"Current speed is {c1.current_speed}")
c1.emergency_brake(-200)
print(f'Current speed is {c1.current_speed}')

#3
class Car:

    def __init__(self,registration_num,maxi_speed,current_speed,travel_distance):
        self.registration_num=registration_num
        self.maxi_speed=maxi_speed
        self.current_speed=current_speed
        self.travel_distance=travel_distance

    def drive(self, constant_time):
        self.travel_distance=int(self.travel_distance + (self.current_speed * constant_time))
        return
c1=Car('ABC-123',142,60,2000)
c1.drive(1.5)
print(f'Current travel distance is {c1.travel_distance}')

#4
import random


class Car:
    def __init__(self, registration_num, maxi_speed, current_speed=0, travel_distance=0):
        self.registration_num = registration_num
        self.maxi_speed = maxi_speed
        self.current_speed = current_speed
        self.travel_distance = travel_distance

    def accelerate(self, delta_speed):
        self.current_speed += delta_speed
        if self.current_speed > self.maxi_speed:
            self.current_speed = self.maxi_speed
        elif self.current_speed < 0:
            self.current_speed = 0
        return

    def drive(self):
        self.accelerate(random_speed(-10, 15))
        distance = self.current_speed * 1
        self.travel_distance += distance
        print(f'Car {self.registration_num} has travelled {self.travel_distance}.')


def random_speed(lower_limit, upper_limit):
    return random.randint(lower_limit, upper_limit)


def race():
    reach_10000 = False
    while not reach_10000:
        for c in car_list:
            c.drive()
            if c.travel_distance >= 10000:
                reach_10000 = True  # for while to stop
                break  # don't change next car in the list


# main starts here
car_list = []
for c in range(10):  # c = 0 -> 9
    car = Car("ABC-" + str(c + 1), random_speed(100, 200))
    car_list.append(car)

print(car_list)

race()
print(car_list)




