import math

class Circle():
    def __init__(self, r):
        self.radius = r

    def circumference(self):
        return self.radius * math.pi * 2

    def area(self):
        return self.radius ** 2 * math.pi

    def volume(self):
        return (4/3) * math.pi * self.radius ** 3