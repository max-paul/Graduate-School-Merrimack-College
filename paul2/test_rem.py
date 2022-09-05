import unittest
from remainder import Remainder


class TestRem(unittest.TestCase):

    #this test should return true as 5 goes into 20 evenly
    def testRem1(self):
        value = Remainder(5, 20).value
        self.assertEqual(value, True)

    # this should return false
    def testRem2(self):
        value = Remainder(3, 67).value
        self.assertEqual(value, False)


if __name__ == '__main__':
    unittest.main()
