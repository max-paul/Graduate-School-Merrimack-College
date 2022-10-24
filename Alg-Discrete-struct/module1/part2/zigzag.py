class ZigZag:
    def __init__(self, a, b, c):
        self.self = self
        self.a = a
        self.b = b
        self.c = c
        self.result = False

    def checkZigZag(self):
        """
        comparing the logic of zig zag here!

        :return: self.result True or False
        """
        if((self.a < self.b and self.b > self.c) or
                (self.a > self.b and self.b < self.c)):
            self.result = True

    def getResult(self):
        """

        :return: returns the result of checking if ZigZag
        """
        return self.result
