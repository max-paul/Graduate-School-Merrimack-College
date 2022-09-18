from random import randint

class Account:
    def __init__(self):
        # accountNumber starts as 0 but has a setter method.
        self.account_number = self.random_account_number(8)
        # initalizing the variables for name
        self.owner_first_name = None
        self.owner_last_name = None
        # a String (not an integer) that contains the 9 digits of the
        # account owner’s social security number
        self.SSN = None
        # randomly generated upon account creation and may start with one or more zeroes
        self.PIN = self.random_pin()
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

    def set_ssn(self):
        loop = True
        while loop:
            #ssn = int(input("Enter your SSN:"))
            ssn = 123456789
            print(len(str(ssn)))
            if len(str(ssn)) == 9:
                self.SSN = ssn
                loop = False
            else:
                print("Social Security Number must be 9 digits")
                continue

    def get_pin(self):
        return self.PIN

    def set_pin(self):
        self.PIN = self.random_pin()

    def set_custom_pin(self):
        loop = True
        while loop:
            custom_pin = str(input("Please enter a custom pin:"))
            if len(custom_pin) != 4:
                print(f"{custom_pin} is not 4 digits")
                continue
            else:
                custom_pin_check = str(input("Please validate the pin:"))
                if custom_pin == custom_pin_check:
                    self.PIN = custom_pin
                    loop = False
                    print("PIN updated")
                else:
                    print("PINS do not match, try again")
                    continue

    def get_balance(self):
        return self.BALANCE

    def set_balance(self,balance):
        self.BALANCE = balance

    def deposit(self, amount):
        self.BALANCE = self.BALANCE + amount
        print(f"New Balance: ${self.get_balance()}")

    def withdraw(self, amount):
        if (self.BALANCE - amount) < 0:
            print(f"Insufficient funds in account {self.account_number}")
            return False
        else:
            self.BALANCE = self.BALANCE - amount
            print(f"New Balance is {self.BALANCE}")
            return True

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
        var = ["============================================================",
               f"Account Number: {self.account_number}",
               f"Owner First Name: {self.owner_first_name}",
               f"Owner Last Name: {self.owner_last_name}",
               f"Owner SSN: {self.SSN}",
               f"PIN: {self.PIN}",
               f"Balance: {self.BALANCE}",
               "============================================================"]
        toPrint = ''
        for i in var:
            toPrint += i + "\n"
        return toPrint

    def random_account_number(self, n):
        range_start = 10 ** (n - 1)
        range_end = (10 ** n) - 1
        num = randint(range_start, range_end)
        if str(num).startswith('0'):
            num.replace('0', str(randint(0, 9)))
        return num

    def random_pin(self):
        range_start = 10 ** (4 - 1)
        range_end = (10 ** 4) - 1
        num = randint(range_start, range_end)
        return str(num)


    def atmWithdraw(self,totalAmount):
        def get_digits(weight_entry):
            out = {}
            entries = ('twenties', 20), ('tens', 10), ('fives', 5)
            for word, num in entries:
                out[word] = weight_entry // num
                weight_entry %= num
            print(f"Returning {int(out['twenties'])} 20s")
            print(f"Returning {int(out['tens'])} 10s")
            print(f"Returning {int(out['fives'])} 5s")
            return out

        if (totalAmount % 5) != 0:
            print("Not a valid mutiple of 5.")
            return False
        else:
            data = get_digits(totalAmount)

