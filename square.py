class Square:
    def __init__(self, side=10):
        self.side = side

    def calculate_area(self):
        return self.side ** 2

    def draw(self):
        for i in range(self.side):
            print(' * ' * self.side)


s1 = Square(5)
s1.draw()
s2 = Square(10)
s2.draw()
print(s1.calculate_area())
print(s2.calculate_area())