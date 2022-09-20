import random


class BankUtility:

    def __init__(self):
        self.self = self



    def isNumeric(self,number):
        if str(number).isnumeric():
            return True
        else:
            return False


    def promtUserForString(self,inputNaming):
        loop = True

        while loop:
            inp = str(input(inputNaming))
            if inp.isalpha():
                loop = False
                return inp
            else:
                print("Please enter a string!")
                loop = True

    def convertFromDollarsToCents(self,money):

        return float(str(money).replace(".",""))

    def promptUserForPositiveNumber(self,inputNaming):
        loop = True
        while loop:
            inp = float(input(inputNaming))
            if inp >= 0:
                return inp
            else:
                print("Amount can not be negative, Try again")
                continue

    def generateRandomInteger(self, min, max):
        num = random.randint(min, max)
        return num