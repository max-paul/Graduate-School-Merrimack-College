import random
import time
import cProfile


def quicksort(array):
    if len(array) <= 1:
        return array
    pivot = array[0]
    left = []
    right = []
    for elem in array[1:]:
        if elem <= pivot:
            left.append(elem)
        else:
            right.append(elem)
    return quicksort(left) + [pivot] + quicksort(right)


def test_sorting_algorithm(sort_func):
    for n in range(1000, 11000, 1000):
        array = [random.randint(1, 100000) for _ in range(n)]
        start_time = time.time()
        sorted_array = sort_func(array)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Sorted {n} elements in {execution_time:.6f} seconds")
        cProfile.runctx('quicksort(array)', globals(), {'array': array})


if __name__ == '__main__':
    test_sorting_algorithm(quicksort)