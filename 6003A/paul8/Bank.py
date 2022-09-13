class Bank:
    def __init__(self):
        self.accounts = []
        self.bank_limit = 100

    def addAccountToBank(self,account):
        self.accounts.append(account)

    def removeAccountFromBank(self,account):
        # implement removeAccountFromBank here
        self.accounts.remove(account)


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
