class Swap:
    def __init__(self):
        self.self = self
        self.vector = None
        self.len = None

    def getLen(self):
        """
        settings the length of the vector 9-21, else if will keep asking
        :return: None
        """
        loop = True
        while loop:
            try:
                self.len = int(input("Please enter a length between 9 and 21:"))
                if self.len <= 21 and self.len >= 9:
                    loop = False
            except Exception as e:
                print(e)

    def createVector(self):
        """

        :return: setting the vector to our len length
        """
        self.vector = list(range(0, self.len, 1))

    def swapPositions(self):
        """
        we swap every odd positions postion with the previous, so 1, 2, 3, 4 becomes 2, 1, 4, 3
        :return: the new vector
        """
        for i in self.vector:
            # this could be improved by iterating ONLY over the odd numbered vector indices.
            # cut wasted loop time, would this perform faster on something like a set/map?
            if i < len(self.vector) - 1 and i % 2 != 0 and self.vector is not None:
                self.vector[i], self.vector[i - 1] = self.vector[i - 1], self.vector[i]
        return self.vector
