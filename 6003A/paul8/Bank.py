
class Bank:
    def __init__(self):
        self.accounts = []
        self.bank_limit = 100

    def addAccountToBank(self,account):
        if len(self.accounts) <= self.bank_limit:

            for i in self.accounts:
                if i.account_number == account.account_number:
                    print("Account Number has been taken!")
                    account.set_account_number()
                    print(f"New Account Num set to {account.account_number}")
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


    def check_limit(self):
        if self.bank_limit > len(self.accounts):
            return True
        else:
            return False

    def findAccount(self,accountNumer):
        for i in self.accounts:
            if i.get_account_number() == accountNumer:
                return i
        else:
            return None


    def addMonthlyInterest(self,interestRate):
        if len(self.accounts) >= 1:
            for i in self.accounts:
                total = i.BALANCE + ((i.BALANCE * ((interestRate/ 100))) / 12)
                total = round(total,2)
                i.set_balance(total)
                print(f"Deposited {round(((i.BALANCE * ((interestRate/ 100))) / 12),2)} into {i.get_account_number()}")

        else:
            print("There are no accounts in the bank!")
