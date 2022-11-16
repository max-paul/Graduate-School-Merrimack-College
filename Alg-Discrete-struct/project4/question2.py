"""
2) Given an array of real numbers, without sorting the array, find the smallest gap between all
pairs of elements (for an array A, the absolute value of the difference between elements 𝐴𝑖 and 𝐴𝑗).
Your function should have one input parameter – an array of numbers – and should return a non-negative
number indicating the smallest gap using a return statement.

Run your algorithm on the problem instances:
a) <50, 120, 250, 100, 20, 300, 200>
b) <12.4, 45.9, 8.1, 79.8, -13.64, 5.09>
"""

def find_smallest_gap(data: list):
    """
    :param data: a list of real numbers
    :return the smallest gap of all nums
    """
    # out final list of gaps between elements
    gapped_data = []

    for i in data:
        # temp_data restarts for each element in the list
        # for each run we store the gaps; then take the lowest from this list
        temp_data = []
        for y in data:
            # if we dont ignore the case where i == y index, then we will always have a 0
            # forcefully removing 0 is not acceptable as its very valid to have a list with 2 same nums
            # we need to handle this edge case
            # by checking if the index is the same we can determine if we want to check or not
            # this will make out alg n-1 faster :)
            if data.index(i) != data.index(y):
                temp_data.append(abs(i-y))
        gapped_data.append(min(temp_data))

    return min(gapped_data)

print(find_smallest_gap([50, 120, 250, 100, 20, 300, 200]))