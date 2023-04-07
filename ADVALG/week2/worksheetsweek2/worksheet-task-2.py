import random

"""

Using the built in python counter module...
from collections import Counter


The most_common method returns a list of the most common elements and their frequencies, 
sorted in descending order. We can retrieve the mode element by accessing the first element 
of the list and then its first element (the mode element itself).

This is a cool and really short hand implementation on finding the mode.

def find_mode_sorted(arr):
    counts = Counter(arr)
    mode = counts.most_common(1)[0][0]
    return mode

"""


def find_mode_sorted(arr):
    arr.sort()
    mode = None
    max_freq = 0
    curr_elem = None
    curr_freq = 0

    for elem in arr:
        if elem != curr_elem:
            if curr_freq > max_freq:
                max_freq = curr_freq
                mode = curr_elem
            curr_elem = elem
            curr_freq = 1
        else:
            curr_freq += 1

    if curr_freq > max_freq:
        mode = curr_elem

    return mode

def getRandomArray():
    # Create an empty array
    arr = []

    # Generate 1000 random integers between 1 and 1,000,000
    for i in range(1000):
        arr.append(random.randint(1, 1000000))# Create an empty array
    return arr

data  = getRandomArray()

mode = find_mode_sorted(data)
print(f"The mode of the data is: {mode}")