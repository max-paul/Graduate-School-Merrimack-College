import random

"""
    -------BATTLESHIPS-------
    Pre-reqs: Loops, Strings, Arrays, 2D Arrays, Global Variables, Methods
    How it will work:
    1. A 10x10 grid will have 5 ships randomly placed about
    2. You can choose a row and column to indicate where to shoot
    3. For every shot that hits or misses it will show up in the grid
    4. If all ships are shot, game over
    Legend:
    1. "." = water
    2. "S" = ship position
    3. "O" = water that was shot with bullet, a miss because it hit no ship
    4. "X" = ship sunk!
"""
# Global variable for grid size
grid_size = 10
# Global variable for grid
grid = [[''] * grid_size for i in range(grid_size)]
# Global variable for number of ships to place
num_of_ships = 5


def drawBoard(myBoard):
    data = '''
|   | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
+---+---+---+---+---+---+---+---+---+---+---
   '''

    for i in range(grid_size):
        add = f'''
| {i} | {myBoard[i][0]} | {myBoard[i][1]} | {myBoard[i][2]} | {myBoard[i][3]} | {myBoard[i][4]} | {myBoard[i][5]} | {myBoard[i][6]} | {myBoard[i][7]} | {myBoard[i][8]} | {myBoard[i][9]} |
+---+---+---+---+---+---+---+---+---+---+---
            '''
        data = data + add
    print(data)


def setupBoard(myBoard):
    # setting everything in the list to .
    for i in range(grid_size):
        for j in range(grid_size):
            myBoard[i][j] = "."
    # now place the ships
    # you can get a random row by using
    # for the range of num_of_ships, randomly place an S
    for i in range(1,num_of_ships,1):
        randomRow = random.randint(0, grid_size - 1)
        randomCol = random.randint(0, grid_size - 1)
        # set the random index to S for ship
        myBoard[randomRow][randomCol] = 'S'
    # return myBoard so we can use it
    return myBoard


def hitOrMiss(myBoard, row, col):
    if myBoard[row][col] == "S":
        print("HIT!!")
        myBoard[row][col] = "X"
    else:
        myBoard[row][col] = "O"
        print("miss")
    return


def isGameOver(myBoard):
    status =[]
    for i in range(grid_size):
        if "S" in myBoard[i]:
            status.append(False)
        else:
            status.append(True)
    if False in status:
        return False
    else:
        return True



def main(myBoard):
    myBoard = setupBoard(myBoard)
    drawBoard(myBoard)
    hitOrMiss(myBoard,0,0)
    print(isGameOver(myBoard))
    # here do everything like
    #   set up the board
    #   till the game is over
    #     draw the board
    #     ask for a row and column and check it is a hit or a miss
    # when the game is over, print that message!
    print('Game over!')


# do not forget to call main!
main(grid)