class ToDoList:
    TO_DO = {}

    def adauga_task(self, **kwargs):
        self.TO_DO.update((kwargs))

    def finalizeaza_task(self, nume):
        self.TO_DO.pop(nume)

    def afiseaza_todo(self):
        print(self.TO_DO.keys())

    def detalii_task(self, nume_task):
        if nume_task in self.TO_DO:
            print(self.TO_DO[nume_task])
        else:
            while True:
                raspuns = input(f"doriti sa adaugati {nume_task} ?").lower()
                if raspuns == "da":
                    self.TO_DO[nume_task] = input("introduceti descrierea")
                    break
                elif raspuns == "nu":
                    print("in regula, o zi buna")
                    break
                else:
                    print("raspuns nerecunoscut")


d = ToDoList()

d.adauga_task(
    cumparaturi="lapte, carne", curat="praf, aspirat", gatit="ciorba, cartofi"
)

d.finalizeaza_task("curat")
d.afiseaza_todo()
d.detalii_task("cumparaturi")
print(d.TO_DO)
