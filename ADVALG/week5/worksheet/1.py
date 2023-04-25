from random import randrange

"""
This code tests the Dynamic Array with different initial size and probability values to find those 
that generate a probability of costly operations of at least 1%. The test function loops through 100,000 
iterations, tracking cheap and costly operations to calculate probabilities. The main function calls test 
for each combination of values. To prevent frequent resizing, we can increase the initial size, resize factor, 
or decrease remove probability. Alternative data structures, such as linked lists or hash tables, can also be 
used depending on the use case.

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
