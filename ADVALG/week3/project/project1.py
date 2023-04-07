with open("sample.txt", "r") as f:
    for line in f:
        line = line.strip().split(",")
        name = line[0]
        price = line[1]
        height = int(line[2])
        width = int(line[3])
        depth = int(line[4])

        print(f"Max volume for {name} at price {price} is {height*width*depth}")