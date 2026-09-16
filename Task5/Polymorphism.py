# Task 4: Polymorphism

# First Class
class SavingsAccount:

    def account_type(self):
        print("This is a Savings Account.")
        print("Savings accounts provide interest on the deposited amount.")


# Second Class
class CurrentAccount:

    def account_type(self):
        print("This is a Current Account.")
        print("Current accounts are mainly used for business transactions.")


# Creating objects
savings = SavingsAccount()
current = CurrentAccount()

# Same method call, different behavior
savings.account_type()
print("----------------------")
current.account_type()