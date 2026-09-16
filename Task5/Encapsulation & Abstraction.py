# Task 5: Encapsulation and Abstraction

from abc import ABC, abstractmethod


# Abstract Class
class BankAccount(ABC):

    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.__balance = balance       # Private attribute

    # Encapsulation: Controlled access to balance
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Amount deposited:", amount)
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print("Amount withdrawn:", amount)
        else:
            print("Insufficient balance or invalid amount.")

    # Getter method
    def get_balance(self):
        return self.__balance

    # Abstract method
    @abstractmethod
    def account_type(self):
        pass


# Child Class
class SavingsAccount(BankAccount):

    # Implementing abstract method
    def account_type(self):
        print("Account Type: Savings Account")


# Creating object
account = SavingsAccount("Ashrutha", 10000)

# Display account information
print("Account Holder:", account.account_holder)
account.account_type()

print("Initial Balance:", account.get_balance())

# Deposit
account.deposit(5000)
print("Balance after deposit:", account.get_balance())

# Withdraw
account.withdraw(2000)
print("Balance after withdrawal:", account.get_balance())