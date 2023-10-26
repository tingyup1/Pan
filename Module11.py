#1
class Publication:
    def __init__(self,P_name):
        self.Pname=P_name
    def print_information(self):
        print(f'This publication name is {self.Pname}')
class Book(Publication):
    def __init__(self,Pname,author,page_count):
        Publication.__init__(self,Pname)
        self.author=author
        self.pagr_count=page_count
    def print_information(self):
        Publication.print_information(self)
        print(f'{self.Pname} author is {self.author} page count:{self.pagr_count}')
class Magazine(Publication):
    def __init__(self,Pname,chief):
        Publication.__init__(self,Pname)
        self.chief_editor=chief
    def print_information(self):
        Publication.print_information(self)
        print(f'{self.Pname} have a chief editor :{self.chief_editor}')
book=Book('Compartment NO.6','Rose Liksom',192)
magazine=Magazine('Donald Duck','Aki Hyyppaa')
book.print_information()
magazine.print_information()


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

