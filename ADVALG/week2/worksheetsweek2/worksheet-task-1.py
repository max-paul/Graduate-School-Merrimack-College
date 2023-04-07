import random


# uniqueness alg from class....
def uniqueSortedTransform(a):
    a.sort()
    for i in range(len(a)):
        if (a[i-1] == a[i]):
            return False
    return True


def uniqueSortedBrute(a):
    ans = True
    for i in range(len(a)):
        for j in range(len(a)):
            if (i!=j) and (a[i] == a[j]):
                ans = False
                break
        if(not ans):
            break
    return ans


def getRandomArray():
    # Create an empty array
    arr = []

    # Generate 1000 random integers between 1 and 1,000,000
    for i in range(1000):
        arr.append(random.randint(1, 1000000))# Create an empty array
    return arr



def runTransFormAndConquer():
    randomData = getRandomArray()
    print(f"Is there a match in the data?: {uniqueSortedTransform(randomData)}")


def runBrute():
    randomData = getRandomArray()
    print(f"Is this data Unique?: {uniqueSortedBrute(randomData)}")

runBrute()