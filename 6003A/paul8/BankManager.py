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

    def promptForAccountNumberAndPIN(self, Bank):

        accNum = int(input("Please enter your account number: "))
        pinNum = str(input("Please enter your pin number: "))

        if len(Bank.accounts) > 0:
            for i in Bank.accounts:
                if i.get_account_number() == accNum and i.get_pin() == pinNum:
                    return i
                if i.get_account_number() != accNum:
                    print(f"Account not found for account number: {accNum} ")
                    if i.get_pin() != pinNum:
                        print("Invalid PIN")
                    return None
        else:
            print("No accounts in the Bank")
            return None



    # our main loop to run the application
    def main(self):
        loop = True
        bank = Bank()
        while loop:
            x = 1
            for i in self.menu_items:
                print(x, ":", i)
                x += 1
            try:
                selection = int(input("Please make a selection from the list, 1-11: "))
                if selection < 1 or selection > 11:
                    raise ValueError
                if selection == 1:
                    try:
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
                        string_data = new_acc.toString()
                        print(string_data)
                        continue
                    except ValueError:
                        print("Invalid Choice")
                        continue
                elif selection == 2:
                    # if provided with the correct information we shold return the data
                    # if we provide bad information tell the user, then continue
                    account = self.promptForAccountNumberAndPIN(bank)
                    # print out the account info
                    print(account)

                elif selection == 3:
                    try:
                        current_account = self.promptForAccountNumberAndPIN(bank)
                        if current_account:
                            current_account.set_custom_pin()
                    except ValueError:
                        print("Invalid Choice")
                        continue
                elif selection == 4:
                    try:
                        # if amount is negative prompt again
                        current_account = self.promptForAccountNumberAndPIN(bank)
                        amount_deposit = float(input("Please enter the amount to deposit: "))
                        if current_account:
                            dep = current_account.deposit(amount_deposit)

                    except ValueError:
                        print("Invalid Choice")
                        continue
                elif selection == 5:
                    try:
                        print("Account to transfer From: ")
                        current_account = self.promptForAccountNumberAndPIN(bank)

                        print("Account to transfer too: ")
                        transfer_account = self.promptForAccountNumberAndPIN(bank)
                        transfer_amount = float(input("How much would you like to transfer?: "))

                        current_account.withdraw(transfer_amount)
                        transfer_account.deposit(transfer_amount)
                    except ValueError:
                        print("Invalid Choice")
                        continue

            except ValueError:
                print("Invalid Choice")
                continue


