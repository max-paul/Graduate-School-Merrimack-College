import random


def generateOnesAndZeroes():
    # Generate a list of 5000 0's and 5000 1's and shuffle it
    arr = [0] * 5000 + [1] * 5000
    random.shuffle(arr)
    return arr


def partition(arr, low, high):
    pivot_index = random.randint(low, high)
    pivot = arr[pivot_index]
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def las_vegas_quick_sort(arr, low, high, tries):
    if low < high:
        pivot_index = partition(arr, low, high)
        if arr[pivot_index] == 1:
            return pivot_index, tries
        tries += 1
        result = las_vegas_quick_sort(arr, low, pivot_index - 1, tries)
        if result is not None:
            return result
        tries += 1
        result = las_vegas_quick_sort(arr, pivot_index + 1, high, tries)
        if result is not None:
            return result
    return None


randomZeroAndOne = generateOnesAndZeroes()
n = len(randomZeroAndOne)

result = las_vegas_quick_sort(randomZeroAndOne, 0, n - 1, 1)

if result is not None:
    print("Found 1 at index", result[0], "after", result[1], "tries")
else:
    print("1 not found in the array")
