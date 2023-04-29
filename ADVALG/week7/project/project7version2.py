from datetime import datetime
from math import log2
import random
"""
Create a program that calls the function myFunction(x) from 0 to 9999 and applies the Hill Climbing algorithm to 
find the value of x that delivers the largest value for the function
"""
def myFunction(x):
    if (x == 0) or x < 0:
        return 0
    elif ((log2(x) * 7) % 17) < (x % 13):
        return (x + log2(x)) ** 3
    elif ((log2(x) * 5) % 23) < (x % 19):
        return (log2(x) * 2) ** 3
    else:
        return (log2(x) ** 2) - x


def hill_climbing():
    # Start with random x 1- 9998
    best_x = random.randint(1, 9998)
    # Evaluate function at x = 1 to get initial best value
    best_value = myFunction(best_x)
    # Loop through all values of x from 2 to 9999
    for x in range(0, 9999):
        # Evaluate function at current value of x
        value = myFunction(x)
        # Check the neighboring values of x
        for neighbor in [x - 1, x + 1]:
            # Evaluate function at neighbor value of x
            neighbor_value = myFunction(neighbor)
            # If neighbor value is higher than best value found so far,
            # update best value and best x
            if neighbor_value > best_value:
                best_value = neighbor_value
                best_x = neighbor
        # If current value is higher than best value found so far,
        # update best value and best x
        if value > best_value:
            best_value = value
            best_x = x
    # Return best x found
    return best_x

# Example usage

result = hill_climbing()
print("Best value found at x = ", result, " with function value = ", myFunction(result))