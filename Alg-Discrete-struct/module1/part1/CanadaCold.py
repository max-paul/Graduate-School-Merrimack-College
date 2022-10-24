class CanadianCold:
    def __init__(self):
        self.self = self
        self.thresholdC = None


    def setThresholdC(self):
        """
        sets the threshold in C from the canadian POV
        :return: None
        """
        temp = int(input("What do you, Canadian, consicer is cold in C0:  "))
        self.thresholdC = temp
    # getter for C
    def getThresholdC(self):
        """

        :return: the threshold set by the canadian
        """
        return self.thresholdC