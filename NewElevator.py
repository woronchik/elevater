from elevator import Elevator

class NewElevator(Elevator):
    def __init__(self, max_floor=10, floor=1):
        super().__init__(max_floor, floor)

    def move(self, floor):
        self.move = floor
        self.floor = self.floor
        if self.move > self.max_floor or self.move < self.floor:
            return 'Неправильный номер этажа, выберите от 1 до 10 этажа'
        else:
            return f'Лифт отправляется с {self.floor} на {self.move} этаж'




el = NewElevator()
print(el.move(11))



