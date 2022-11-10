from Tree import Tree

def readFile():
    """
    our operational method for reading in the txt file!

    :return: list of nums from txt file
    """
    nums = []
    file = open("numbers.txt", "r")
    for i in file:
        nums.append(int(i.strip("\n")))
    return nums

def main():

    # Create a program that reads a list of numbers from a text file named “numbers.txt”
    data = readFile() # ["34","12","8","13","55"]
    # using your exact numbers from example to show that it works; please use any numbers you feel needed


    # create a binary tree ordered as the example presented in class
    myTree = Tree(data)
    for x in data:
        myTree.insert(int(x))

    #From the tree structure you have created, create
    # and print a adjacency matrix that represents the graph
    # equivalent to the tree, considering an edge from the node
    # to its child with weight the absolute value of the difference
    # between the numbers of the nodes
    myTree.printAdjMatrix()

    '''
    output -> 
    [[0, 22, 0, 0, 21],
    [0, 0, 4, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]]
    '''


if __name__ == "__main__":
    main()