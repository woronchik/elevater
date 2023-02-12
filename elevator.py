class Elevator:
    def __init__(self, max_floor=5, floor=3):
        self.max_floor = max_floor
        self.floor = floor

    def up(self):
        if self.floor == self.max_floor:
            return "Лифт не может подняться выше"
        else:
            self.floor += 1
            return "Лифт поднимается на {self.floor} этаж"

    def down(self):
        if self.floor == 1:
            return "Лифт не может опуститься ниже"
        else:
            self.floor -= 1
            return "Лифт опускается на {self.floor} этаж"

el = Elevator()
