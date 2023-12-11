class BankAccount:  # CamelCase or PascalCase for naming convention
    """BankAccount stores users with the"""

    def __init__(self, owner, iban):  # minimum req attributes
        # here we define the attributes of the object always with self.
        self.account_owner = owner
        self.iban = iban
        self.balance = 0
        self.active = False
        self.pin = 7777
        self.nr_tries = 4

    def greeting(self):
        print(f"Hello {self.account_owner}!")

    def display(self):
        self.greeting()
        print(f"Account owner is {self.account_owner}")
        print(f"the IBAN is  {self.iban}")
        print(f"Your balance is {self.balance}")
        print(f"Account activated: {self.active}")
        print("---------------------------------")

    def activation(self, pin_client):
        self.greeting()
        if self.active:
            print("account already activated")
        elif pin_client == self.pin:
            self.active = True
            print("account activated successfully")
        else:
            self.nr_tries -= 1
            print(f"Wrong PIN, you have {self.nr_tries} more tries")
        print("------------------------------------------------------")

    def deposit(self, amount):
        self.greeting()
        self.balance += amount
        print(f"deposit successfully {self.balance}")
        print("-----------------------------------------------")

    def card_payment(self, amount):
        self.greeting()
        if amount <= self.balance:
            self.balance -= amount
            print(f"you spent {amount}, current balance {self.balance}")
        else:
            print("insufficient funds")
        print("----------------------------------------------------------")




