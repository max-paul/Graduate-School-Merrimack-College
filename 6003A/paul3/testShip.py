from battleship import setupBoard,isGameOver, hitOrMiss
import unittest
# test for is game over true and false

# setupboard, make sure 5 spaces have S and the rest are "."
        # two tests
#check hit or miss



class TestShip(unittest.TestCase):

    # testing if the game is over
    def testOverFalse(self):
        # setting up our game grid
        grid_size = 10
        grid = [[''] * grid_size for i in range(grid_size)]
        # calling setupBoard to initialize the board with the ships
        myBoard = setupBoard(grid)
        # the board has empty AND ships the games not over
        self.assertEqual(isGameOver(myBoard), False)

    def testOverTrue(self):
        # setting up our game grid
        grid_size = 10
        grid = [[''] * grid_size for i in range(grid_size)]
        # the board has empty and we never setupBoard so we never added the ships
        # this returns True
        self.assertEqual(isGameOver(grid), True)


    def testShipCount(self):
        # initializing var to count ships we see
        shipCount = 0
        # setting up our game grid
        grid_size = 10
        grid = [[''] * grid_size for i in range(grid_size)]
        # calling setupBoard to initialize the board with the ships
        myBoard = setupBoard(grid)

        # looping over board
        for i in range(grid_size):
            for j in range(grid_size):
                #everytime we see a ship lets add
                if myBoard[i][j] == "S":
                    shipCount += 1

        # we should have 5 ships
        self.assertEqual(shipCount, 5)

    def testCountEmpty(self):
        emptyCount = 0
        # setting up our game grid
        grid_size = 10
        grid = [[''] * grid_size for i in range(grid_size)]
        # calling setupBoard to initialize the board with the ships
        myBoard = setupBoard(grid)
        for i in range(grid_size):
            for j in range(grid_size):
                if myBoard[i][j] == ".":
                    emptyCount += 1
        self.assertEqual(emptyCount, 95)

    def testHit(self):
        # setting up our game grid
        grid_size = 10
        grid = [[''] * grid_size for i in range(grid_size)]
        # calling setupBoard to initialize the board with the ships
        myBoard = setupBoard(grid)

        # forcefully setting a ship in place 0 , 0 so this test works everytime as ship placement is random
        myBoard[0][0] = "S"

        # checking a hit or miss in place 0,0 so index 0,0 should be changed to X
        result = hitOrMiss(myBoard, 0, 0)
        # testing the method returns hit
        self.assertEqual(result, "HIT")

    def testMiss(self):
        # setting up our game grid
        grid_size = 10
        grid = [[''] * grid_size for i in range(grid_size)]
        # calling setupBoard to initialize the board with the ships
        myBoard = setupBoard(grid)

        # forcefully setting a blank in place 0 , 0 so this test works everytime as ship placement is random
        myBoard[0][0] = "."

        # checking a hit or miss in place 0,0 so index 0,0 should be changed to X
        result = hitOrMiss(myBoard, 0, 0)

        # testing the method returns miss
        self.assertEqual(result, "MISS")


if __name__ == '__main__':
    unittest.main()
