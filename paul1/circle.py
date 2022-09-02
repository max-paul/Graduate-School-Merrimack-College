import numpy as np


class Circle():
    def __init__(self, r):
        self.radius = r

    def circumference(self):
        return self.radius * np.pi * 2

    def area(self):
        return self.radius ** 2 * np.pi

    def volume(self):
        return (4/3) * np.pi * self.radius ** 3