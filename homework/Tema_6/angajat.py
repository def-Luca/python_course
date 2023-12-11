class Angajat:
    nume = None
    prenume = None
    salariu = 0

    def __init__(self, nume, prenume, salariu):
        self.nume = nume
        self.prenume = prenume
        self.salariu = salariu

    def descrie(self):
        print(f"{self.nume} {self.prenume}, salariu de {self.salariu}")

    def nume_complet(self):
        return f"nume: {self.nume}, prenume:{self.prenume}"

    def salariu_anual(self):
        return self.salariu * 12

    def marire_salariu(self, procent_marire):
        self.salariu = self.salariu + (self.salariu * procent_marire / 100)


luca = Angajat("Ioan", "Luca", 3000)
luca.descrie()
print(luca.nume_complet())
print(luca.salariu_anual())
luca.marire_salariu(10)
print(luca.salariu)
print(luca.salariu_anual())
