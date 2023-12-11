class Masina:
    culoare = "gri"
    viteza_actuala = 0
    culori_disponibile = {"alb", "negru", "rosu", "albastru", "bej"}
    marca = "Dacia"
    inmatriculata = False

    def __init__(self, model, viteza_maxima):
        self.model = model
        self.viteza_maxima = viteza_maxima

    def descrie(self):
        print(
            self.culoare,
            self.viteza_actuala,
            self.marca,
            self.inmatriculata,
            self.model,
            self.viteza_maxima,
        )

    def inmatriculare(self):
        self.inmatriculata = True

    def vopseste(self, culoare):
        if culoare.lower() in self.culori_disponibile:
            self.culoare = culoare
        else:
            print("culoare indisponibila")

    def accelereaza(self, viteza):
        if viteza < 0:
            print("eroare")
            return
        elif viteza <= self.viteza_maxima:
            self.viteza_actuala = viteza
        else:
            self.viteza_actuala = self.viteza_maxima

    def franeaza(self):
        self.viteza_actuala = 0


masina = Masina("Logan", 150)
masina.descrie()
masina.inmatriculare()
masina.vopseste("alb")
masina.accelereaza(100)
masina.descrie()
masina.franeaza()
masina.descrie()
