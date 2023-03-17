'''
Create a program that randomizes a vector of 1000
positive and negative integers, then it finds the
maximum contiguous subsequence sum value
- Prints out the maximum value


Extends the program of Task #1 to output not only
the maximum value, but also the initial and final
index of the elements to compute the maximum
value
'''

import random

vector = [random.randint(-100, 100) for _ in range(1000)]
max_sum = current_sum = start_idx = end_idx = 0

for i, num in enumerate(vector):
    current_sum = max(num, current_sum + num)
    if current_sum == num:
        start_idx = i
    max_sum = max(max_sum, current_sum)
    if max_sum == current_sum:
        end_idx = i

print("Maximum contiguous subsequence sum value:", max_sum)
print("Starting index:", start_idx)
print("Ending index:", end_idx)