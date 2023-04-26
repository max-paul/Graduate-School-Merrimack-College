"""
Create a program that receives the list of possible named items with the following information:

○ Value ($), Height (in), Width (in), Depth (in)

The limit of the optimal solution is expressed by the volume in cubic inches (in3) and the program has to maximize the value within the cubic limit
Your program should read textual file with one item kind per line with the information separated by comma, for example this fileLinks to an external site. list four items with values 35, 40, 45, and 58 dollars and increasing dimensions
Your program should read any file with this format (name, value, height, width, depth) per line
This program must be your own, do not use someone else’s code


"""
from knapsack import knapsack
with open("sample.txt", "r") as f:
    # Parse the items from the file
    items = []
    for line in f:
        # Split the line by comma and remove any whitespace
        line = line.strip().split(",")
        # Extract the values from the split line and assign them to variables
        name = line[0]
        price = int(line[1])
        height = int(line[2])
        width = int(line[3])
        depth = int(line[4])

        # Add the item to the list
        items.append((name, price, height, width, depth))

    # Calculate the maximum total value and selected items using the knapsack function
    max_value, selected_items = knapsack(items, max_volume)

    # Print the results
    print(f"Maximum total value: {max_value}")
    print("Selected items:")
    for name, price in selected_items:
        print(f"{name} at price {price}")

