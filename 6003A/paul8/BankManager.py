from Account import Account
from Bank import Bank
from BankUtility import BankUtility

BU = BankUtility()
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
    def getSelection(self, index):
        return self.menu_items[index - 1]

    def promptForAccountNumberAndPIN(self, Bank):

        accNum = int(input("Please enter your account number: "))
        pinNum = str(input("Please enter your pin number: "))
        if len(Bank.accounts) > 0:
            for i in Bank.accounts:
                if i.get_account_number() == accNum:
                    if i.get_pin() == pinNum:
                        return i
                    else:
                        continue
                else:
                    continue
        else:
            print("No accounts in the Bank")
            return None

    def non_negative_dollar(self, dollars):
        if dollars < 0:
            return True
        else:
            return False

    # our main loop to run the application
    def main(self):
        loop = True
        bank = Bank()
        while loop:
            print(bank.accounts)
            x = 1
            valid_options = 11
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
                        first_name = "max" #BU.promtUserForString("Please Enter your first name: ")
                        last_name = "paul" #BU.promtUserForString("Please Enter your last name: ")
                        new_acc.set_ssn()
                        new_acc.set_owner_first_name(first_name)
                        new_acc.set_owner_last_name(last_name)
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
                    if account != None:
                        print(account.toString())

                elif selection == 3:
                    try:
                        current_account = self.promptForAccountNumberAndPIN(bank)
                        if current_account != None:
                            current_account.set_custom_pin()
                    except ValueError:
                        print("Invalid Choice")
                        continue
                elif selection == 4:

                    # if amount is negative prompt again
                    current_account = self.promptForAccountNumberAndPIN(bank)
                    # ask for amount to dp
                    if current_account != None:
                        amount = BU.promptUserForPositiveNumber("Enter amount to deposit in dollars and cents (e.g 2.57): ")
                        current_account.deposit(amount)

                elif selection == 5:
                    print("Account to transfer From: ")
                    current_account = self.promptForAccountNumberAndPIN(bank)
                    print("Account to transfer too: ")
                    transfer_account = self.promptForAccountNumberAndPIN(bank)

                    if current_account != None or transfer_account != None:
                        transfer_amount = BU.promptUserForPositiveNumber("How much would you like to transfer?: ")

                        # if withdraw was a success then we can deposit.
                        status = current_account.withdraw(transfer_amount)
                        if status:
                            transfer_account.deposit(transfer_amount)

                elif selection == 6:
                    current_account = self.promptForAccountNumberAndPIN(bank)
                    if current_account != None:
                        withdraw = BU.promptUserForPositiveNumber("How much would you like to withdraw?: ")
                        current_account.withdraw(withdraw)

                elif selection == 7:
                    current_account = self.promptForAccountNumberAndPIN(bank)
                    if current_account != None:
                        withdraw = BU.promptUserForPositiveNumber("Enter Amount to withdraw in dollars (no cents) "
                                                                  "in multiples of 5")
                        current_account.atmWithdraw(withdraw)
                        current_account.withdraw(withdraw)

                    '''
                    put in number and calculate the amount per 20 10 and 5
        
                    '''

                elif selection == 11:
                    loop = False
                elif selection > 11:
                    "Invalid Choice"
                    continue
            except ValueError:
                print("Invalid Input, please try again.")
                continue
