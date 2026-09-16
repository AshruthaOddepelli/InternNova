# Task 3: Inheritance

# Parent/Base Class
class BankAccount:

    def __init__(self, account_holder, account_number, balance):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance

    # Common method
    def display_details(self):
        print("Account Holder:", self.account_holder)
        print("Account Number:", self.account_number)
        print("Balance:", self.balance)


# Child/Derived Class
class SavingsAccount(BankAccount):

    def __init__(self, account_holder, account_number, balance, interest_rate):
        # Calling parent class constructor
        super().__init__(account_holder, account_number, balance)
        self.interest_rate = interest_rate

    # Child-specific method
    def calculate_interest(self):
        interest = self.balance * self.interest_rate / 100
        print("Interest Earned:", interest)


# Creating an object of child class
account1 = SavingsAccount(
    "Ashrutha",
    "ACC101",
    50000,
    5
)

# Using inherited method
account1.display_details()

# Using child-specific method
account1.calculate_interest()