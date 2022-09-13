# using random to generate our random number
import random


# creating our sorting class
class Sorting:
    # creating the constructor
    def __init__(self):
        self.self = self
        self.data = []

    # creating a large number list
    def makeBigList(self):
        randomlist = random.sample(range(0, 10000), 2000)
        self.data = randomlist

    # implementing selection sort
    def selection_sort(self):
        for idx in range(len(self.data)):
            min_idx = idx
            for j in range(idx + 1, len(self.data)):
                if self.data[min_idx] > self.data[j]:
                    min_idx = j
                    # Swap the minimum value with the compared value
                self.data[idx], self.data[min_idx] = self.data[min_idx], self.data[idx]
        return self.data

    # implementing bubble sort
    def bubblesort(self):
        # Swap elements to arrange in order
        for iter_num in range(len(self.data) - 1, 0, -1):
            for idx in range(iter_num):
                if self.data[idx] > self.data[idx + 1]:
                    temp = self.data[idx]
                    self.data[idx] = self.data[idx + 1]
                    self.data[idx + 1] = temp
        return self.data
