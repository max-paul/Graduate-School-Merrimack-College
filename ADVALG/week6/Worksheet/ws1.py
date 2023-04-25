"""

A fancy food truck makes pizzas and sandwiches:

A pizza is sold for $50 and it costs $25 to make
A sandwich is sold for $20 and it costs $5 to make
It takes 8 minutes to prepare a pizza, and it takes 3 minutes to prepare a sandwich

MAIN QUESTION:
Assuming that the food truck has only one hour (sixty minutes) to prepare food,
how many pizzas and sandwiches should be made to maximize the profit?

"""
# Define the cost and time requirements of each item
# The cost is the amount of money it costs to make each item
# The price is the amount of money each item is sold for
# The time is the number of minutes it takes to prepare each item
pizza_cost = 25
pizza_price = 50
pizza_time = 8
sandwich_cost = 5
sandwich_price = 20
sandwich_time = 3

# Define the maximum preparation time in minutes
# This is the total amount of time available for food preparation
max_time = 60

# Define the variables for the optimal solution
# These variables will be updated as we find better solutions
optimal_profit = 0
optimal_pizzas = 0
optimal_sandwiches = 0

# Try all possible combinations of pizzas and sandwiches
# We use nested loops to iterate over all possible combinations
for pizzas in range(max_time // pizza_time + 1):
    for sandwiches in range(max_time // sandwich_time + 1):

        # Calculate the total preparation time and cost for this combination
        # This is the time and cost required to make the current combination of pizzas and sandwiches
        total_time = pizzas * pizza_time + sandwiches * sandwich_time
        total_cost = pizzas * pizza_cost + sandwiches * sandwich_cost

        # If the total preparation time is within the limit, calculate the profit
        # We only consider solutions where the total preparation time is less than
        # or equal to the maximum available time
        if total_time <= max_time:
            total_profit = pizzas * pizza_price + sandwiches * sandwich_price - total_cost

            # If the profit is greater than the current optimal profit, update the variables
            # We keep track of the best solution we have found so far
            if total_profit > optimal_profit:
                optimal_profit = total_profit
                optimal_pizzas = pizzas
                optimal_sandwiches = sandwiches

# Print the optimal solution
# This prints out the number of pizzas and sandwiches to make and the total profit achieved
print("Number of Pizzas: ", optimal_pizzas)
print("Number of Sandwiches: ", optimal_sandwiches)
print("Total Profit: $", optimal_profit)
