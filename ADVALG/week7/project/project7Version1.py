from math import log2

"""
Create a program that calls the function myFunction(x) from 0 to 9999 and applies the Hill Climbing algorithm to find the value of x that delivers the largest value for the function
Implement a version where the initial search value x is chosen randomly between the values 1 to 9998
You can use this function to test your program, but your program should work with any version of myFunction(x)
def myFunction(x):
    if (x == 0) or x < 0:
        return 0
    elif ((log2(x) * 7) % 17) < (x % 13):
        return (x + log2(x)) ** 3
    elif ((log2(x) * 5) % 23) < (x % 19):
        return (log2(x) * 2) ** 3
    else:
        return (log2(x) ** 2) - x

"""

"""
we can implement any function for this hill climbing algorithm as long as it only takes in one param of x.
else we will need to modify the params passed into the method within hill_climbing().

as the instructions state; "but your program should work with any version of myFunction(x)"... i am interpreting this as a single param method
where x is an int.

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

    """
    A hill climbing algorithm is a type of problem-solving method that is used to find the best possible solution to a problem.
    The algorithm starts with an initial solution and then tries to improve it by making incremental changes to it.
    The goal is to climb up a metaphorical "hill" of possible solutions until the algorithm reaches the best solution, or the highest point on the hill.

    At each step, the algorithm evaluates the current solution and its neighboring solutions to determine which one is the best. If a neighboring solution is better,
    it becomes the new current solution and the process repeats until no further improvements can be made.

    The hill climbing algorithm is often used in optimization problems, such as finding the shortest path between two points or maximizing the efficiency of a system.
    However, it is important to note that the algorithm may not always find the absolute best solution, as it can sometimes get stuck in a local maximum instead of
    reaching the global maximum.


    """

    # Start with x = 0
    best_x = 0
    # Evaluate function at x = 0 to get initial best value
    best_value = myFunction(best_x)
    # Loop through all values of x from 2 to 9999
    for x in range(0, 9999,3): # skipping 3 places as we check neighbors +/- 1
        # Evaluate function at current value of x
        value = myFunction(x)
        # Check the neighboring values of x
        for neighbor in [x - 1, x + 1]:
            # Evaluate function at neighbor value of x
            neighbor_value = myFunction(neighbor)
            # Update best value and best x if neighbor value is higher
            if neighbor_value > best_value or value > best_value:
                best_value = neighbor_value if neighbor_value > value else value
                best_x = neighbor if neighbor_value > value else x
    # Return best x found
    return best_x


result = hill_climbing()
print("Best value found at x = ", result, " with function value = ", myFunction(result))
