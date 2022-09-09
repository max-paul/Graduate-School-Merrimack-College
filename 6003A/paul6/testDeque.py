from deque import Deque
import unittest

'''

Our unit Testing basis based from requirements:

The radius should equal the input of the class
The circumference of a circle with a radius of 2.750 is 17.27875

The area of a circle with a radius of 2.750 is 23.75827

The volume of a sphere with a radius of 2.750 is 87.11367
'''


class TestingDeque(unittest.TestCase):

    # making sure the length of the deque is 0
    def testCreateDequeEmpty(self):
        deq = Deque()
        self.assertEqual(len(deq.items), 0)

    # testing adding an item and making sure the len is over 1
    def testAddItemToDeque(self):
        deq = Deque()
        deq.addFront("max")
        self.assertEqual(len(deq.items), 1)

    # adding something to the front and testing
    def testAddtoFront(self):
        deq = Deque()
        # initial the deque
        deq.addFront("paul")
        # adding this item to the front
        deq.addFront("max")
        self.assertEqual(deq.items[0], "max")

    # testing that we add something to the back of the que
    def testAddToBack(self):
        deq = Deque()
        # initial the deque
        deq.addFront("paul")
        # adding this item to the front
        deq.addBack("max")
        self.assertEqual(deq.items[-1], "max")



if __name__ == '__main__':
    unittest.main()