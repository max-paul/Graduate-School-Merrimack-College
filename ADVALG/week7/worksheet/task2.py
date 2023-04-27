import random

# Generate random array with equal number of 0's and 1's
arr = [0] * 5000 + [1] * 5000
random.shuffle(arr)

def monteCarloSearch(arr):
    # Implement randomized Monte Carlo algorithm to search for 1
    k = 10
    tries = 0
    while tries < k:
        index = random.randint(0, len(arr)-1)
        if arr[index] == 1:
            print(f"Found 1 at position {index+1} after {tries+1} tries")
            break
        tries += 1
    else:
        print(f"Failed to find 1 after {tries} tries")


monteCarloSearch(arr)

