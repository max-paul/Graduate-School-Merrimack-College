# importing our class as well as the needed time class to generate the time to operate our algorithms
from sort import Sorting
import time


def main():
    # initilizing an object for each sorting method
    selection_sort = Sorting()
    bubble_sort = Sorting()

    # creating a big list for each of our objects
    selection_sort.makeBigList()
    bubble_sort.makeBigList()

    # starting the timer for selection sort
    start_time_selection_sort = time.time()
    # implementing selection sort
    sorted_selection = selection_sort.selection_sort()
    # the time taken to do the selection sort
    timeTakenSelection = time.time() - start_time_selection_sort
    print(f"Time Taken for selection sort: {round(timeTakenSelection * 1000)}ms")

    # starting the timer for bubble sort
    start_time_bubble_sort = time.time()
    # doing the bubble sort
    sorted_bubble = bubble_sort.bubblesort()
    # the time taken to implement the bubble sort
    timeTakenBubble = time.time() - start_time_bubble_sort
    print(f"Time taken for bubble sort: {round(timeTakenBubble*1000)}ms")


main()