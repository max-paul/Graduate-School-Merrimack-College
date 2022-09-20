import unittest
from CoinCollector import CoinCollector
from Account import Account
from Bank import Bank
from BankUtility import BankUtility

class TestingBank(unittest.TestCase):

    def test_coin_collector_one(self):
        # should equal .40
        coinDeposits = "dddd"
        collector = CoinCollector(coinDeposits)
        collector.parseChange()
        self.assertEqual(collector.totalCoinValue, .40)

    def test_coin_collector_two(self):
        coinDeposits = "QDtqwd"
        collector = CoinCollector(coinDeposits)
        collector.parseChange()
        self.assertEqual(collector.totalCoinValue, 1.50)

    def test_coin_collector_three(self):
        coinDeposits = "sglobf"
        collector = CoinCollector(coinDeposits)
        collector.parseChange()
        self.assertEqual(collector.totalCoinValue, 0)


    def test_deposit(self):
        new_acc = Account()
        bank = Bank()
        # create the account
        # get input we need to get
        first_name = "Max"
        last_name = "Paul"
        new_acc.SSN = 123456789
        new_acc.set_owner_first_name(first_name)
        new_acc.set_owner_last_name(last_name)
        status = bank.addAccountToBank(new_acc)
        amount = 10.00
        new_acc.deposit(amount)
        self.assertEqual(new_acc.BALANCE, 10.00)



    #withdraw
    def test_withdraw(self):
        new_acc = Account()
        bank = Bank()
        # create the account
        # get input we need to get
        first_name = "Max"
        last_name = "Paul"
        new_acc.SSN = 123456789
        new_acc.set_owner_first_name(first_name)
        new_acc.set_owner_last_name(last_name)
        status = bank.addAccountToBank(new_acc)
        amount = 10.00
        new_acc.deposit(amount)
        # withdrawing
        new_acc.withdraw(5.00)
        self.assertEqual(new_acc.BALANCE, 5.00)


    # is valid pin
    def test_valid_pin(self):
        new_acc = Account()
        bank = Bank()
        # create the account
        # get input we need to get
        first_name = "Max"
        last_name = "Paul"
        new_acc.SSN = 123456789
        new_acc.set_owner_first_name(first_name)
        new_acc.set_owner_last_name(last_name)
        new_acc.PIN = 1234
        status = bank.addAccountToBank(new_acc)
        self.assertEqual(new_acc.PIN, 1234)

    def test_add_account(self):
        new_acc = Account()
        bank = Bank()
        # create the account
        # get input we need to get
        first_name = "Max"
        last_name = "Paul"
        new_acc.SSN = 123456789
        new_acc.set_owner_first_name(first_name)
        new_acc.set_owner_last_name(last_name)
        new_acc.PIN = 1234
        status = bank.addAccountToBank(new_acc)
        self.assertEqual(len(bank.accounts), 1)

    def test_remove_account(self):
        new_acc = Account()
        bank = Bank()
        # create the account
        # get input we need to get
        first_name = "Max"
        last_name = "Paul"
        new_acc.SSN = 123456789
        new_acc.set_owner_first_name(first_name)
        new_acc.set_owner_last_name(last_name)
        new_acc.PIN = 1234
        status = bank.addAccountToBank(new_acc)
        bank.removeAccountFromBank(new_acc)
        self.assertEqual(len(bank.accounts), 0)

    def test_find_account(self):
        new_acc = Account()
        bank = Bank()
        # create the account
        # get input we need to get
        first_name = "Max"
        last_name = "Paul"
        new_acc.SSN = 123456789
        new_acc.set_owner_first_name(first_name)
        new_acc.set_owner_last_name(last_name)
        new_acc.PIN = 1234
        status = bank.addAccountToBank(new_acc)
        account = bank.findAccount(new_acc.account_number)
        self.assertEqual(Account, type(Account()))

    def test_is_numeric(self):
        BU = BankUtility()
        self.assertEqual(BU.isNumeric("1"), True)


    def test_convert_dollars_cents(self):
        BU = BankUtility()
        total = BU.convertFromDollarsToCents(1.35)
        self.assertEqual(total, .135)

    def test_generate_random_int(self):
        BU = BankUtility()
        num = BU.generateRandomInteger(1,100)
        self.assertEqual(type(num), int)

if __name__ == '__main__':
    unittest.main()