"""
1. Create a new class for a CustomerBankAccount.

2. Create fields for the Account Number, Balance, Customer Name, Email and Phone Number.

3. Create methods to read, write and update each field. Basically, some getters and setters.

4. Create two additional methods:
   i. One to allow the customer to deposit the funds (this should increment the balance field)
   ii. One to allow the customer to withdraw funds (this should deduct from the balance fields but not allow the withdrawal to complete if their founds are insufficient).

5. Create some validation code using your getters and setters to confirm your code is working at each step of the user flow. You should be able to show that a new user can be created and that this user can deposit and withdraw funds.

6. Now that you've learned about Class Inheritance, let's create some subclasses of the standard BankAccount. First, let's create a StandardCustomerBankAccount with additional fields for tracking Silver Reward Points and tracking Reward Order Transactions. Let's mock the Reward Order Transactions as a list of string objects for now.

7. Create a new class VipCustomer that can earn both Silver and Gold reward points in addition to also having Reward Order Transactions.

8. Create getters and setters for each new field, and implement some validation to confirm your code is working.

9. Let's now create a new Rewards class to represent prizes that customers can exchange reward points for. Fields should include the object name and object price in terms of both Silver and Gold points.

10. We now need to create subclasses of the Rewards Class. We want to be able to distinguish between tangible, physical objects that can be purchased, and digital purchases such as credits towards one's balance.
    i. DigitalRewards should have a conversion rate. Because Silver points and Gold points have different perceived values, they should reduce a customer's monetary balance at different rates.
    ii. PhysicalRewards will need an inventory count, because they are not infinitely available like digital rewards are.
    iii. Create getter, setter functions for all these new fields, and implement validation to confirm your code is working as intended.
"""


class CustomerBankAccount:
    def __init__(self, account_number, balance, name, email, phone):
        self.__account_number = int(account_number)
        self.__balance = int(balance)
        self.__name = name
        self.__email = email
        self.__phone = phone

    def __str__(self):
        return f"Account #: {self.__account_number}\nBalance: {self.__balance}\nName: {self.__name}\nE-Mail: {self.__email}\nPhone: {self.__phone}"

    # Getters
    def get_acct_number(self):
        return self.__account_number

    def get_balance(self):
        return self.__balance

    def get_name(self):
        return self.__name

    def get_email(self):
        return self.__email

    def get_phone(self):
        return self.__phone

    # Setters
    def set_acct_number(self, value):
        self.__account_number = value

    def set_balance(self, value):
        self.__balance = value

    def set_name(self, value):
        self.__name = value

    def set_email(self, value):
        self.__email = value

    def set_phone(self, value):
        self.__phone = value

    # Customer deposits, increments balance attribute.
    def deposit(self, amount):
        amount = int(amount)
        self.__balance += amount

    # Customer withdrawal, must have enough in account.
    def withdraw(self, amount):
        amount = int(amount)
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            return "Insufficient funds."


# Tests
if __name__ == "__main__":
    acct1 = CustomerBankAccount(321, 500, "Steve", "email", "123-4567")
    print("Account Info:")
    print("-------------")
    print(acct1)
    print("-------------")
    print("Add a new deposit of $100")
    acct1.deposit(100)
    print(f"New account balance: {acct1.get_balance()}")
    print("Create a withdrawal of $200")
    acct1.withdraw(200)
    print(f"New account balance: {acct1.get_balance()}")
    print("Try to withdraw more than you have available.")
    print(acct1.withdraw(600))
    print(acct1.get_balance())
