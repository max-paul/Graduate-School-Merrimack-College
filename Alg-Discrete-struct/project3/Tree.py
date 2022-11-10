from pprint import pprint

class Node:
    def __init__(self, d):
        self.Data, self.Left, self.Right = d, None, None


class Tree:
    def __init__(self, data, d=None):
        self.data = data
        self.iteration = 0
        if (d == None): # an empty tree
            self.Root = None
        else:
            self.Root = Node(d)
    def insert(self, d):
        def __insertHere__(n, d):
            if (n.Data > d):   # if no node left insert here
                if (n.Left == None):
                    n.Left = Node(d)
                else:          # or try left child
                    __insertHere__(n.Left, d)
            elif (n.Data < d): # if no node right insert here
                if (n.Right == None):
                    n.Right = Node(d)
                else:          # or try right child
                    __insertHere__(n.Right, d)
        if (self.Root == None): # it was an empty tree
            self.Root = Node(d)
        else:
            if (self.Root.Data > d):          # try left child
                if (self.Root.Left == None):  # if empty insert here
                    self.Root.Left = Node(d)
                else:                         # try left subtree
                    __insertHere__(self.Root.Left, d)
            elif (self.Root.Data < d):        # try right child
                if (self.Root.Right == None): # if empty insert here
                    self.Root.Right = Node(d)
                else:                         # try right subtree
                    __insertHere__(self.Root.Right, d)
    def check(self, d):
        def __check__(n, d):
            if (n == None):
                return False
            elif (n.Data == d):
                return True
            elif (n.Data > d):
                return __check__(n.Left, d)
            elif (n.Data < d):
                return __check__(n.Right, d)
        return __check__(self.Root, d)
    def printInorder(self):
        def __visit__(n):
            if (n != None):
                __visit__(n.Left)
                print(n.Data, end=" ")
                __visit__(n.Right)
        print("\n--------")
        __visit__(self.Root)
        print("\n--------")
    def printPreorder(self):
        def __visit__(n, h):
            if (n != None):
                print("---"*h, n.Data)
                __visit__(n.Left, h+1)
                __visit__(n.Right, h+1)
        print("^^^^^^^^^^")
        __visit__(self.Root, 1)
        print("^^^^^^^^^^")
    def printPostorder(self):
        def __visit__(n, h):
            if (n != None):
                __visit__(n.Left, h+1)
                __visit__(n.Right, h+1)
                print("---"*h, n.Data)
        print("==========")
        __visit__(self.Root, 1)
        print("==========")

    def createMatrix(self, number):
        matrix = [[0 for i in range(number)] for j in range(number)]


        return matrix

    def printAdjMatrix(self):
        matrix = self.createMatrix(len(self.data))

        def __visit__(n, matrix):
            if (n != None):

                if (n.Left != None or n.Right != None):
                    currentNode = n.Data
                    inputData = self.data
                    # try left
                    try:
                        currentLeft = n.Left.Data
                        leftWeight = abs(currentNode - currentLeft)
                        indexLeft = inputData.index(int(currentLeft))

                        matrix[self.iteration][indexLeft] = leftWeight
                    except:
                        pass

                    try:
                        currentRight = n.Right.Data
                        rightWeight = abs(currentNode - currentRight)
                        indexRight = inputData.index(int(currentRight))
                        matrix[self.iteration][indexRight] = rightWeight
                    except:
                        pass
                    self.iteration+=1
                else:
                    # if we have nothing to hanlde
                    self.iteration+=1


                __visit__(n.Left, matrix)
                __visit__(n.Right, matrix)
        print("\n--------")
        __visit__(self.Root, matrix)
        pprint(matrix)
        print("\n--------")