class Cont:
    def __init__(self, iban, titular_cont, sold):
        self.iban = iban
        self.titular_cont = titular_cont.capitalize()
        self.sold = sold

    def afisare_sold(self):
        print(f"titularul {self.titular_cont} are in contul {self.iban
        }, suma de {self.sold}")

    def debitare_cont(self, debitare):
        self.sold = self.sold - debitare

    def creditare_cont(self, creditare):
        self.sold = self.sold + creditare

marcel = Cont("RO123", "marcel", 100 )

marcel.afisare_sold()

marcel.debitare_cont(150)
marcel.afisare_sold()

marcel.creditare_cont(250)
marcel.afisare_sold()