'''
3. Bank Account Simulation

Create classes for Account, SavingsAccount, and CurrentAccount.

Demonstrate polymorphism for account_type() and calculate_interest() methods.
Add private attributes and use getters/setters.
'''
import random

class Account:
    total_customers = 0
    total_money_in_the_bank = 0
    overall_customer_detail = {}
    saving_account_record = {}
    current_account_record = {}

    def __init__(self, account_number, account_holders_name, amount):
        self.account_number = account_number
        self.account_holders_name = account_holders_name
        self.amount = int(amount)
        Account.overall_customer_detail[account_number]=self
        Account.total_customers+=1
        Account.total_money_in_the_bank+=self.amount
        print('\nNew account created')
        print(f'Name: {account_holders_name}')
        print(f'Account number: {account_number}')
        print(f'Amount: {amount}')
    
    @classmethod
    def add_amount(cls, self, additional_amount):
        self.amount+=additional_amount
        cls.total_money_in_the_bank+=cls.total_money_in_the_bank
        return self.amount
    @classmethod
    def withdrawn_amount(cls, self, withdrawn_amount):
        self.amount-=withdrawn_amount
        cls.total_money_in_the_bank-=cls.total_money_in_the_bank
        return self.amount
    @classmethod
    def remove_account(cls, account_number):
        cls.total_customers-=1
        amount_to_be_removed = cls.overall_customer_detail[account_number].amount
        cls.total_money_in_the_bank-=amount_to_be_removed
        if account_number in Account.saving_account_record:
            del cls.saving_account_record[account_number]
            print('Successfully removed from savings account database!')
        elif account_number in Account.current_account_record:
            del cls.saving_account_record[account_number]
            print('Successfully removed from current account database!')
        del cls.overall_customer_detail[account_number]
        print('Successfully removed from overall database!')
        return True
    
    @classmethod
    def get_bank_details(cls):
        print(f'Following the account numbers present: {cls.overall_customer_detail.keys()}')

    def account_type(cls, self):
        pass

class SavingsAccount(Account):
    def __init__(self, account_number, account_holders_name, amount):
        super().__init__(account_number, account_holders_name, amount)
        Account.saving_account_record[self.account_number]=self

    def calculate_interest(self, days):
        interest_percentage = 10
        interest  = self.amount * interest_percentage * days /100
        return interest
    
    def account_type(self):
        print('Account Type: Savings Account')
        return True

class CurrentAccount(Account):
    def __init__(self, account_number, account_holders_name, amount):
        super().__init__(account_number, account_holders_name, amount)
        Account.current_account_record[self.account_number]=self

    def calculate_interest(self, days):
        interest_percentage = 20
        interest  = self.amount * interest_percentage * days / 100
        return interest
    
    def account_type(self):
        print('Account Type: Current Account')
        return True



def main():
    print('Enter 1 to Create new account')
    print('Enter 2 to remove an existing account')
    print('Enter 3 to add money in existing account')
    print('Enter 4 to widthdraw money from existing account')
    print('Enter 5 to know account type')
    selection_input= int(input('Enter your choice: '))
    if selection_input == 1:
        pass
#testing code
account_1 = SavingsAccount(random.randint(100000,999999), 'Rohit Tiwari', 10000)
Account.get_bank_details()
print(f'Interest is {account_1.calculate_interest(365)}')
account_1.account_type()
print(Account.total_money_in_the_bank)
Account.remove_account(account_1.account_number)
Account.get_bank_details()
print(Account.total_money_in_the_bank)