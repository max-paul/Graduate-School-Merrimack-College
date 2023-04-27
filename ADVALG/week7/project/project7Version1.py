from math import log2

def myFunction(x):
    if (x == 0):
        return 0
    elif ((log2(x) * 7) % 17) < (x % 13):
        return (x + log2(x)) ** 3
    elif ((log2(x) * 5) % 23) < (x % 19):
        return (log2(x) * 2) ** 3
    else:
        return (log2(x) ** 2) - x

def hill_climbing():
    # Start with x = 1
    best_x = 0
    # Evaluate function at x = 1 to get initial best value
    best_value = myFunction(best_x)
    # Loop through all values of x from 2 to 9999
    for x in range(0, 9999):
        # Evaluate function at current value of x
        value = myFunction(x)
        # If current value is higher than best value found so far,
        # update best value and best x
        if value > best_value:
            best_value = value
            best_x = x
    # Return best x found
    return best_x

result = hill_climbing()
print("Best value found at x = ", result, " with function value = ", myFunction(result))
