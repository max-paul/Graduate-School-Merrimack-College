from circle import Circle
import unittest

'''

Our unit Testing basis based from requirements:

The radius should equal the input of the class
The circumference of a circle with a radius of 2.750 is 17.27875

The area of a circle with a radius of 2.750 is 23.75827

The volume of a sphere with a radius of 2.750 is 87.11367
'''


class TestingCircle(unittest.TestCase):

    def testRadius(self):
        radius = Circle(2.75).radius
        self.assertEqual(radius, 2.75)

    def testArea(self):
        area = Circle(2.75).area()
        self.assertEqual(area, 23.75829444277281)

    def testCircumference(self):
        circumference = Circle(2.75).circumference()
        self.assertEqual(circumference, 17.27875959474386)

    def testVolume(self):
        volume = Circle(2.75).volume()
        self.assertEqual(volume, 87.11374629016697)

if __name__ == '__main__':
    unittest.main()