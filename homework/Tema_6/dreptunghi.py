class Dreptunghi:
    lungime = 0
    latime = 0
    culoare = None

    def __init__(self, lungime, latime, culoare):
        self.lungime = lungime
        self.latime = latime
        self.culoare = culoare

    def descrie(self):
        print(f"L {self.lungime}, l {self.latime} si culoare {self.culoare}")

    def aria(self):
        return self.lungime * self.latime

    def perimetru(self):
        return self.lungime * 2 + self.latime * 2

    def schimba_culoarea(self, noua_culoare):
        self.culoare = noua_culoare


drept = Dreptunghi(10, 5, "verde")
print(drept.aria())
print(drept.perimetru())
drept.schimba_culoarea("rosu")
drept.descrie()
