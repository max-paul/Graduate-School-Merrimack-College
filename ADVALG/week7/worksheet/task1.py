import random

def generateOnesAndZeroes():
    # Generate a list of 5000 0's and 5000 1's and shuffle it
    arr = [0] * 5000 + [1] * 5000
    random.shuffle(arr)
    return arr
def randomized_search(list):
    tries=0
    while True:
        tries+=1
        index = random.randint(0, len(list)-1)
        if list[index] == 1:
            return index,tries

# Generate a list of 5000 0's and 5000 1's, shuffle it, and store it in a variable
randomZeroAndOne = generateOnesAndZeroes()
# Get the length of the list
n = len(randomZeroAndOne)
# Perform Las Vegas QuickSort on the list to find the index of the first occurrence of 1
result = randomized_search(randomZeroAndOne)

# Print the result
if result is not None:
    print("Found 1 at index", result[0], "after", result[1], "tries")
else:
    print("1 not found in the array")

