import random

# Generate random array with equal number of 0's and 1's
def generateOnesAndZeroes():
    # Generate a list of 5000 0's and 5000 1's and shuffle it
    arr = [0] * 5000 + [1] * 5000
    random.shuffle(arr)
    return arr

k = 10

def monteCarlo(arr, k):
    # implement the randomized Monte Carlo algorithm
    tries = 0
    found = False
    while tries < k and not found:
        # randomly select an index in the array
        index = random.randint(0, len(arr)-1)
        # check if the element at the selected index is a 1
        if arr[index] == 1:
            found = True
            # output the position of the first 1 found and the number of tries
            print("The first 1 is at position", index, "found after", tries+1, "tries")
        else:
            tries += 1

    # output a message if no 1 is found after k tries
    if not found:
        print("No 1 found after", k, "tries")

arr = generateOnesAndZeroes()
monteCarlo(arr, k)
