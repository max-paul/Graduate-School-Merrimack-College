class Bank:
    def __init__(self):
        self.accounts = []
        self.bank_limit = 100

    def addAccountToBank(self,account):
        if len(self.accounts) <= self.bank_limit:
            self.accounts.append(account)
            return True
        else:
            print("No More accounts available")
            return False

    def removeAccountFromBank(self,account):
        # implement removeAccountFromBank here
        try:
            self.accounts.remove(account)
            print("Account Successfully Removed")
        except ValueError:
            print(f"Account Not Found for account number: {self.accounts.account_number}")


    def validate_user(self,accNum,pinNum):
        for i in self.accounts:
            if i.get_account_number() == accNum and i.get_pin() == pinNum:
                return i
            elif i.get_account_number() != accNum:
                print(f"Account not found for account number: {accNum} ")
            elif i.get_pin() != pinNum:
                print(f"Account not found for pin number: {pinNum} ")

    def check_limit(self):
        if self.bank_limit > len(self.accounts):
            return True
        else:
            return False

    def findAccount(self,accountNumer):
        for i in self.accounts:
            if i.get_account_number():
                return i
        else:
            return None


    def addInterest(self,interestRate):
        if len(self.accounts) >= 1:
            for i in self.accounts:
                total = i.BALANCE + ((i.BALANCE * ((interestRate/ 100))) / 12)
                total = round(total,2)
                i.set_balance(total)
                print(f"Deposited {round(((i.BALANCE * ((interestRate/ 100))) / 12),2)} into {i.get_account_number()}")

        else:
            print("There are no accounts in the bank!")
