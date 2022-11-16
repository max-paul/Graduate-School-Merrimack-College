"""
1) Find the number of entries in an array of integers that are divisible by a given integer. Your function should have two input parameters – an array of integers and a positive integer – and should return an integer indicating the count using a return statement.
Run your algorithm on the problem instances:
a) [20, 21, 25, 28, 33, 34, 35, 36, 41, 42] number of entries that are divisible by 7
and
b) [18, 54, 76, 81, 36, 48, 99] number of entries that are divisible by 9
"""


def count_divisible(data: list, divisor: int):
    """
    :method:
    count_divisible: a method where we use two inputs; to determine the total count of whole divisible integers

    :input:
    data: an array / list of integers
    divisor: a positive int

    :return:
    count: the count of divisible without remainder
    """
    counter = 0
    for i in data:
        if i%divisor==0:
            counter+=1

    return counter

total_divisible = count_divisible([20, 21, 25, 28, 33, 34, 35, 36, 41, 42],13)

print(total_divisible)