'''
Create a program that randomizes a vector of 1000
positive and negative integers, then it finds the
maximum contiguous subsequence sum value
- Prints out the maximum value
'''

import random

#vector = [random.randint(-100, 100) for _ in range(1000)]
vector = [-2, 34, -16, 9, -32, 12, 38, -1, 81, -76, 9, 34, -4, 12]
# defining our needed vars together
max_sum = current_sum = 0
for num in vector:
    '''
    current_sum using the max() function to ensure that it is always greater than or equal to zero.
    It then updates max_sum to be the maximum of the current max_sum and current_sum.
    
    This does what we saw in class in two lines of code and one loop.
    '''
    current_sum = max(0, current_sum + num)
    max_sum = max(max_sum, current_sum)

print("Maximum contiguous subsequence sum value:", max_sum)