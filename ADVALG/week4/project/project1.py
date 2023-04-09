"""
Create a program that receives the list of possible named items with the following information:

○ Value ($), Height (in), Width (in), Depth (in)

The limit of the optimal solution is expressed by the volume in cubic inches (in3) and the program has to maximize the value within the cubic limit
Your program should read textual file with one item kind per line with the information separated by comma, for example this fileLinks to an external site. list four items with values 35, 40, 45, and 58 dollars and increasing dimensions
Your program should read any file with this format (name, value, height, width, depth) per line
This program must be your own, do not use someone else’s code


"""

# Open the file for reading
with open("sample.txt", "r") as f:
    # Iterate over each line in the file
    for line in f:
        # Split the line by comma and remove any whitespace
        line = line.strip().split(",")

        # Extract the values from the split line and assign them to variables
        name = line[0]
        price = line[1]
        height = int(line[2])
        width = int(line[3])
        depth = int(line[4])

        # Calculate the max volume and print the result
        max_volume = height * width * depth
        print(f"Max volume for {name} at price {price} is {max_volume}")
