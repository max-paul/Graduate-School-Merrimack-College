"""

Using a for loop, write a code fragment that counts backward from 50 to 25 by 5’s and only prints out the values 50, 45, 40…etc. until 25.
Using a do-while loop, write a code fragment that reads a String from the keyboard from the user until the user types “EXIT”
Examine the code from at least two of your classmates and provide your feedback and suggestions.

"""

class Counter:
    def __init__(self, start, stop, step):
        self.self=self
        self.start = start
        self.stop = stop
        self.step = step

    def countBackwards(self):
        for i in range(self.start,self.stop,self.step):
            print(i)

class doWhile:
    def __init__(self):
        self.self=self

    def doWhileInput(self):
        loop = True
        while loop:
            inp = input("Enter anything! enter EXIT to close loop: ")
            print(inp)
            if inp == "EXIT":
                loop = False

Counter(50,20,-5).countBackwards()
doWhile().doWhileInput()