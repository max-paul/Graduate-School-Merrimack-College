from Account import Account
from Bank import Bank
class BankManager:
    # settings our constructor
    def __init__(self):
        self.self = self
        self.menu_items = [
                           "Open Account",
                           "Get account information and balance",
                           "Change PIN",
                           "Deposit money into account",
                           "Transfer money between accounts",
                           "Withdraw money from an account",
                           "Make an ATM withdrawal from an account",
                           "Deposit change into an account",
                           "Close an account",
                           "Add monthly interest to all accounts",
                           "End Program"
                           ]

    # function to handle our menu selection
    def getSelection(self,index):
        return self.menu_items[index-1]


    # our main loop to run the application
    def main(self):
        loop = True
        bank = Bank()
        while loop:
            x = 1
            for i in self.menu_items:
                print(x ,":", i)
                x += 1
            try:
                selection = int(input("Please make a selection from the list, 1-11: "))
                if selection < 1 or selection > 11:
                    raise ValueError
                if selection == 1:
                    new_acc = Account()
                    # create the account
                    # get input we need to get
                    first_name = str(input("Please Enter your first name: "))
                    last_name = str(input("Please Enter your last_name name: "))
                    ssn = int(input("Please Enter your SSN: "))
                    new_acc.set_owner_first_name(first_name)
                    new_acc.set_owner_last_name(last_name)
                    new_acc.set_ssn(str(ssn))
                    new_acc.set_pin()
                    new_acc.set_account_number()
                    new_acc.toString()
                    bank.addAccountToBank(new_acc)
                    # check if account number already exists ??
                    continue
                elif selection == 2:
                    # if provided with the correct information we shold return the data
                    accNum = int(input("Please enter your account number: "))
                    pinNum = str(input("Please enter your pin number: "))
                    bank.showAccount(accNum, pinNum)
                    continue
                elif selection == 3:
                    accNum = int(input("Please enter your account number: "))
                    pinNum = str(input("Please enter your pin number: "))
                    current_account = bank.validate_user(accNum,pinNum)
                    if current_account:
                        current_account.set_custom_pin()
                elif selection == 4:
                    accNum = int(input("Please enter your account number: "))
                    pinNum = str(input("Please enter your pin number: "))
                    current_account = bank.validate_user(accNum, pinNum)
                    amount_deposit = float(input("Please enter the amount to deposit: "))
                    if current_account:
                        current_account.deposit(amount_deposit)



            except ValueError:
                print("Invalid Choice")
                continue


