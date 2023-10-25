#1
class Elevator:
    def __init__(self, bottom_floors, top_floors):
        self.bottom_floors = bottom_floors
        self.top_floors = top_floors
        self.current_floor = bottom_floors

    def go_to_floor(self, destination_floor):
        if destination_floor < self.bottom_floors:
            destination_floor = self.bottom_floors
        elif destination_floor > self.top_floors:
            destination_floor = self.top_floors
        while self.current_floor < destination_floor:
            self.floor_up()
        while self.current_floor > destination_floor:
            self.floor_down()

    def floor_up(self):
        if self.current_floor < self.top_floors:
            self.current_floor += 1
            print(f'Elevator is on {self.current_floor}')

    def floor_down(self):
        if self.current_floor > self.bottom_floors:
            self.current_floor -= 1
            print(f'Elevator is on {self.current_floor}')


h=Elevator(0,7)
h.go_to_floor(5)


#2
class Elevator:
    def __init__(self,bottom_floors,top_floors):
        self.bottom_floors=bottom_floors
        self.top_floors=top_floors
        self.current_floor = bottom_floors

    def go_to_floor(self,destination_floor):
       if destination_floor<self.bottom_floors:
           destination_floor=self.bottom_floors
       elif destination_floor>self.top_floors:
           destination_floor=self.top_floors
       while self.current_floor < destination_floor:
           self.floor_up()
       while self.current_floor > destination_floor:
           self.floor_down()

    def floor_up(self):
        if self.current_floor < self.top_floors:
            self.current_floor+=1
            print(f'Elevator is on {self.current_floor}')
    def floor_down(self):
        if self.current_floor > self.bottom_floors:
            self.current_floor-=1
            print(f'Elevator is on {self.current_floor}')


class Building:
    def __init__(self,bFloor,tFloor,numElevator):
        self.bottom=bFloor
        self.top=tFloor
        self.elevators_list = []
        for i in range(numElevator):
            self.elevators_list.append(Elevator(bFloor,tFloor))

    def run_elevator(self,elevator_num,destination_floor):
        if elevator_num<0 or elevator_num >= len(self.elevators_list):
            print(f'Invalid number.Correct number between 0 - {len(self.elevators_list)-1}')
            return
        if destination_floor<self.bottom or destination_floor > self.top:
            print(f'We have not construct {destination_floor} floor!')
            return
        elevator = self.elevators_list[elevator_num]
        elevator.go_to_floor(destination_floor)


building1=Building(0,7,3)
building2=Building(5,7,3)
building1.run_elevator(1,8)
building2.run_elevator(1,3)


#3

class Elevator:
    def __init__(self,bottom_floors,top_floors):
        self.bottom_floors=bottom_floors
        self.top_floors=top_floors
        self.current_floor = bottom_floors

    def go_to_floor(self,destination_floor):
       if destination_floor<self.bottom_floors:
           destination_floor=self.bottom_floors
       elif destination_floor>self.top_floors:
           destination_floor=self.top_floors
       while self.current_floor < destination_floor:
           self.floor_up()
       while self.current_floor > destination_floor:
           self.floor_down()

    def floor_up(self):
        if self.current_floor < self.top_floors:
            self.current_floor+=1
            print(f'Elevator is on {self.current_floor}')
    def floor_down(self):
        if self.current_floor > self.bottom_floors:
            self.current_floor-=1
            print(f'Elevator is on {self.current_floor}')


class Building:
    def __init__(self,bFloor,tFloor,numElevator):
        self.bottom=bFloor
        self.top=tFloor
        self.elevators_list = []
        for i in range(numElevator):
            self.elevators_list.append(Elevator(bFloor,tFloor))

    def run_elevator(self,elevator_num,destination_floor):
        if elevator_num<0 or elevator_num >= len(self.elevators_list):
            print(f'Invalid number.Correct number between 0 - {len(self.elevators_list)-1}')
            return
        if destination_floor<self.bottom or destination_floor > self.top:
            print(f'We have not construct {destination_floor} floor!')
            return
        elevator = self.elevators_list[elevator_num]
        elevator.go_to_floor(destination_floor)

    def fire_alarm(self):
        print("Alarm!!!")
        for i in self.elevators_list:
            i.go_to_floor(self.bottom)

building=Building(0,10,2)
building.run_elevator(1,6)
building.fire_alarm()

#4

