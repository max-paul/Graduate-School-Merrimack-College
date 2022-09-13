from random import randint

class Account:
    def __init__(self):
        # accountNumber starts as 0 but has a setter method.
        self.account_number = 0
        # initalizing the variables for name
        self.owner_first_name = ''
        self.owner_last_name = ''
        # a String (not an integer) that contains the 9 digits of the
        # account owner’s social security number
        self.SSN = ""
        # randomly generated upon account creation and may start with one or more zeroes
        self.PIN = 0
        # represents the balance in cents
        self.BALANCE = 0
        # add methods as getters and setters for attributes
        # getters and setters

    def get_account_number(self):
        return self.account_number

    def set_account_number(self):
        self.account_number = self.random_account_number(8)

    def get_owner_first_name(self):
        return self.owner_first_name

    def set_owner_first_name(self, new_owner_first_name):
        self.owner_first_name = new_owner_first_name

    def get_owner_last_name(self):
        return self.owner_last_name

    def set_owner_last_name(self, new_owner_last_name):
        self.owner_last_name = new_owner_last_name

    def get_ssn(self):
        return self.SSN

    def set_ssn(self,SSN):
        self.SSN = SSN

    def get_pin(self):
        return self.PIN

    def set_pin(self):
        self.PIN = self.random_pin()

    def set_custom_pin(self):
        custom_pin = str(input("Please enter a custom pin:"))
        custom_pin_check = str(input("Please validate the pin:"))

        if custom_pin == custom_pin_check:
            self.PIN = custom_pin


    def get_balance(self):
        return self.balance

    def deposit(self, amount):
        self.BALANCE += amount
        return 0

    def withdraw(self,amount):
        self.BALANCE -= amount
        return 0  # be sure to change this

    def isValidPIN(self,pin):
        # implement isValidPIN here
        if pin == self.PIN:
            return True
        else:
            return False  # be sure to change this

    def isValidAccountNumber(self,accountNum):
        # implement isValidPIN here
        if accountNum == self.account_number:
            return True
        else:
            return False  # be sure to change this


    def toString(self):
        print("============================================================")
        print(f"Account Number: {self.account_number}")
        print(f"Owner First Name: {self.owner_first_name}")
        print(f"Owner Last Name: {self.owner_last_name}")
        print(f"Owner SSN: {self.SSN}")
        print(f"PIN: {self.PIN}")
        print(f"Balance: ${self.BALANCE}")
        print("============================================================")

    def random_account_number(self, n):
        range_start = 10 ** (n - 1)
        range_end = (10 ** n) - 1
        num = randint(range_start, range_end)
        s = '0'+ str(num)
        if s.startswith('0'):
            s.replace('0', str(randint(0, 9)))
        return num

    def random_pin(self):
        range_start = 10 ** (4 - 1)
        range_end = (10 ** 4) - 1
        num = randint(range_start, range_end)
        return str(num)
