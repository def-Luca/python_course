from learn.OOP.bank_account_def import BankAccount

b = BankAccount("Luca Ioan", "RO1234")

b.activation(6666)
b.activation(7777)
b.display()

b.deposit(250)
b.card_payment(300)
b.card_payment(150)
