

class CoinCollector:
    def __init__(self, CoinString: str):
        self.self = self
        self.CoinString = CoinString
        self.totalCoinValue = 0

    def parseChange(self):
        total = 0
        if str(self.CoinString).isalpha():
            for i in self.CoinString.upper():
                if i == "P":
                    total += .01
                elif i == "N":
                    total += .05
                elif i == 'D':
                    total += .1
                elif i == "Q":
                    total += .15
                elif i == "H":
                    total += .5
                elif i == "W":
                    total +=1
            self.totalCoinValue = total





