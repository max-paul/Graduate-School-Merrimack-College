# importing base collection for deque functionality
from collections import deque

#initializing the deque


class Deque:
    def __init__(self):
        self.self = self
        self.items = deque([])

    def showQue(self):
        # this prints item in the que
        print(self.items)

    def addFront(self,item):
        # will add items to the front
        self.items.appendleft(item)

    def addBack(self,item):
        # will add items to the back
        self.items.append(item)



