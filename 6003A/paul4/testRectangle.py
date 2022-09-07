from Rectangle import Rectangle,Parallelepipede
import unittest

'''

Our unit Testing basis based from requirements:

The radius should equal the input of the class
The circumference of a circle with a radius of 2.750 is 17.27875

The area of a circle with a radius of 2.750 is 23.75827

The volume of a sphere with a radius of 2.750 is 87.11367
'''


class TestingRectangle(unittest.TestCase):

    def testPerimeter(self):
        perimeter = Rectangle(2,3).Perimeter()
        self.assertEqual(perimeter, 10)

    def testArea(self):
        area = Rectangle(2,3).Area()
        self.assertEqual(area, 6)

    def testParallelepipede(self):
        volume = Parallelepipede(2,3,2).volume()
        self.assertEqual(volume, 12)

if __name__ == '__main__':
    unittest.main()