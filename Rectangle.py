from square import Square

class Rectangle(Square):
    def __init__(self, side=5, height=10):
        super().__init__(side)
        self.height = height

    def calculate_area(self):
        return f'Площадь фигуры равна: {self.side * self.height}'

    def draw(self):
        print(" * " * self.height)
        for _ in range(self.side):
            print(" * " * (self.height))
        print(" * " * self.height)


r1 = Rectangle()
r1.draw()
r2 = Rectangle(5, 3)
r2.draw()

print(r1.calculate_area())
print(r2.calculate_area())
