from elevator import Elevator

class NewElevator(Elevator):
    def __init__(self, max_floor=10, floor=1):
        super().__init__(max_floor, floor)



    def move(self, floor):
        self.move = floor
        self.floor = self.floor
        if self.move > self.max_floor or self.move < 1:
            print('Неправильный номер этажа')
        else:
            return f'Лифт отправляется с {self.floor} этажа на {self.move} этаж'





fl = NewElevator()
print(fl.move(2))

