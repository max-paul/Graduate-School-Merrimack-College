class Bank:
    def __init__(self):
        self.accounts = []
        self.bank_limit = 100

    def addAccountToBank(self,account):
        self.accounts.append(account)

    def removeAccountFromBank(self,account):
        # implement removeAccountFromBank here
        self.accounts.remove(account)

    def findAccount(self,accountNumber):
        for i in self.accounts:
            if accountNumber == i.get_account_number():
                return True
            else:
                return False

    def showAccount(self,accNum,pinNum):
        for i in self.accounts:
            if i.get_account_number() == accNum and i.get_pin() == pinNum:
                i.toString()
            else:
                print('wrong')

    def validate_user(self,accNum,pinNum):
        for i in self.accounts:
            if i.get_account_number() == accNum and i.get_pin() == pinNum:
                return i

    def check_limit(self):
        if self.bank_limit > len(self.accounts):
            return True
        else:
            return False
