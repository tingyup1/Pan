#1
class Book:
    def __init__(self,name,author,page_count):
        self.name=name
        self.author=author
        self.page_count=page_count

class  Chief_editor(Book):
    def __init__(self,name,author,page_count,chief):
        Book.__init__(self,name,author,page_count)    #or super().__init__(name,author,page_count)
        self.chief=chief

    def print_information(self):
        print(f'Book name:{self.name},Author:{self.author},Page count:{self.page_count},Chief_editor:{self.chief}')
book=Book( 'Donald Duck','Rosa Liksom',192)
book=Chief_editor('Donald Duck','Rosa Liksom',192, 'Aki Hyyppä')
book.print_information()

#2
class Car:
    def __init__(self,registration_num,maxi_speed):
        self.registration_num=registration_num
        self.maxi_speed=maxi_speed
        self.kilo_counter=0

    def drive(self,hours):
        self.kilo_counter+=self.maxi_speed*hours
class ElectricCar(Car):
    def __init__(self,registration_num,maxi_speed,battery_capacity):
        Car.__init__(self,registration_num,maxi_speed)
        self.battery_capacity=battery_capacity

class GasolineCar(Car):
    def __init__(self,registration_num,maxi_speed,tank_volume):
        Car.__init__(self,registration_num,maxi_speed)
        self.tank_volume=tank_volume



electric_car=ElectricCar('ABC-15',180,52.5)
gasoline_car=GasolineCar('ACD-123', 165, 32.3)
electric_car.drive(3)
gasoline_car.drive(3)
print(f'Electric Car Kilometer Counter:{electric_car.kilo_counter}')
print(f'Gasoline Car Kilometer Counter:{gasoline_car.kilo_counter}')

