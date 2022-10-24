class Temperature:
    def __init__(self, C):
        self.self = self
        self.F = None
        self.C = C

    def convert_f_to_c(self):
        """
        converts the degress F to degrees C

        :return: Degrees in celcius
        """
        conversion = int((self.F-32)*(5/9))
        return conversion

    def setF(self):
        """
        input todays temp in F
        :return: sets Self.F
        """
        temp = int(input("What is today's temp in F: "))
        self.F = temp

    def isCold(self):
        """
        our main logic comparing F and C

        :return: Whether its cold or not
        """
        print("Temperature Threshold: ", self.C, "C")
        print("Today's Temp: ", self.F, "F")
        print("Todays Temp in F, Converted to C: ", self.convert_f_to_c(), "C")
        if self.convert_f_to_c() > self.C:
            return "Not Cold"
        elif self.convert_f_to_c() == self.C:
            return "Set Threshold is same as current temp :)"
        else:
            return "Cold"