class Remainder:
    # initialize the vars needed for calculation
    def __init__(self,num1,num2):
        self.self = self
        self.num1 = num1
        self.num2 = num2
        # perform the calc to view if either remainder returns 0
        if self.num1 % self.num2 == 0 or self.num2 % self.num1 == 0:
            # if remainder is 0 set class level param to True
            self.value = True
        else:
            # if remainder is not  0 set class level param to False
            self.value = False

