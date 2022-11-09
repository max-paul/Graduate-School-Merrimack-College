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
    data = readFile()
    myTree = Tree(data)
    for x in data:
        myTree.insert(int(x))
    myTree.printtest()

    # build the weighted edges



main()