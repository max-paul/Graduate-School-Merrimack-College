"""
Implement a Double Array Queue and test it for a very large case (100,000 randomly decided operations of enqueue or dequeue)

Your program should compute the number of costly operations and cheap operations

Your program should also ask the user about the ratio between enqueue and dequeue operations:

The probability of enqueues and dequeues should never be of less than half enqueues than dequeues (33% enqueues - 67%)
The probability of enqueues and dequeues should never be of less than half dequeues than enqueues (67% enqueues - 33%)
This program must be your own, do not use someone else’s code

Any specific questions about it, please bring to the Office hours meeting this Friday or contact me by email

This is a challenging program to make sure you are mastering your Python programming skills, as well as your asymptotic analysis understanding. Don’t be shy with your questions

"""

import random

class DoubleArrayQueue:
    def __init__(self):
        # Initialize the empty queue with an empty array and set front and rear pointers
        self.arr = []
        self.front = 0
        self.rear = -1

    def enqueue_front(self, data):
        # Add data to the front of the queue and increment rear pointer
        self.arr.insert(self.front, data)
        self.rear += 1

    def enqueue_rear(self, data):
        # Add data to the end of the queue and increment rear pointer
        self.arr.append(data)
        self.rear += 1

    def dequeue_front(self):
        # Remove data from the front of the queue and decrement rear pointer
        if self.is_empty():
            return None
        data = self.arr.pop(self.front)
        self.rear -= 1
        return data

    def dequeue_rear(self):
        # Remove data from the end of the queue and decrement rear pointer
        if self.is_empty():
            return None
        data = self.arr.pop()
        self.rear -= 1
        return data

    def is_empty(self):
        # Check if the queue is empty
        return self.size() == 0

    def size(self):
        # Calculate the size of the queue
        return self.rear - self.front + 1


if __name__ == '__main__':
    n = 100000
    daq = DoubleArrayQueue()
    costly_ops = 0
    cheap_ops = 0

    # Get input from user for ratio of enqueue/dequeue operations
    while True:
        enqueue_ratio = float(input("Enter the probability of enqueue operations (between 0.34 and 0.66): "))
        if 0.34 <= enqueue_ratio <= 0.66:
            break
        print("Invalid input. Please try again.")

    # Perform operations on queue
    for i in range(n):
        operation = random.random()
        if operation <= enqueue_ratio:
            # Perform enqueue operation
            daq.enqueue_front(i)
            cheap_ops += 1
        else:
            # Perform dequeue operation
            if daq.is_empty():
                # If queue is empty, add new data to front and increment costly ops counter
                daq.enqueue_front(i)
                costly_ops += 1
            else:
                # If queue is not empty, remove data from rear and increment cheap ops counter
                daq.dequeue_rear()
                cheap_ops += 1

    # Print final queue size and number of costly and cheap operations
    print("Final queue size: ", daq.size())
    print("Number of cheap operations: ", cheap_ops)
    print("Number of costly operations: ", costly_ops)
