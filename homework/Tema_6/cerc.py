class Cerc:
    PI = 3.14159
    raza = 0
    culoare = None

    def __init__(self, raza, culoare):
        self.raza = raza
        self.culoare = culoare

    def descrie_cerc(self):
        print(self.culoare)

    def aria(self):
        return self.PI * self.raza**2

    def diametru(self):
        return self.raza * 2

    def circumferinta(self):
        return self.PI * self.raza * 2


c = Cerc(3.14, "verde")

c.descrie_cerc()
print(c.aria())
print(c.diametru())
print(c.circumferinta())
