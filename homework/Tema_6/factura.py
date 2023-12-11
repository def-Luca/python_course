import pandas as pd


class Factura:
    import pandas as pd
    from datetime import date

    serie = 123456
    data = date.today()

    def __init__(self, nume_produs, cantitate, pret_bucata):
        self.nume_produs = nume_produs
        self.cantitate = cantitate
        self.pret_bucata = pret_bucata
        self.pret_total = cantitate * pret_bucata

    def schimba_cantitate(self, cantitate):
        self.cantitate = cantitate
        self.pret_total = self.pret_bucata * cantitate

    def genereaza_factura(self):
        print(f"Data {self.data}")
        return pd.DataFrame(
            [
                [
                    self.serie,
                    self.nume_produs,
                    self.cantitate,
                    self.pret_bucata,
                    self.pret_total,
                ]
            ],
            columns=["serie", "denumire", "cantitate", "pret_unitar", "pret_total"],
            index=["valori"],
        )


factura = Factura("proteine", 2, 100)

factura.schimba_cantitate(4)
print(factura.cantitate)
print(factura.genereaza_factura())
factura2 = Factura("lapte", 1, 5)
print(factura2.genereaza_factura())
