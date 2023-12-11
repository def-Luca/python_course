print ("1. Declara o lista note_muzicale in care sa pui do re mi etc pana la do")

note_muzicale = ["do", "re", "mi", "fa", "sol", "la", "si", "do"]
# print(note_muzicale)
# note_muzicale = note_muzicale[::-1]
# print(note_muzicale)
# note_muzicale.reverse() # metoda reverse pe liste o inverseaza
# print(note_muzicale)

print("2. De cate ori apare do? ")

# print(note_muzicale.count("do")) # functia count, numara de cate ori apare un elem intr o lista

print("3. ai 2 liste, gaseste 2 metode sa le unesti")

lista1 = [3, 0, 1, 2]
lista2 = [6, 4, 5]

# lista3 = lista1 + lista2
# lista3.reverse()
# print(lista3)
lista_unita = lista1.__add__(lista2) # modul __add__ uneste 2 liste, sau simplu cu plus
print(lista_unita)

print("4. Sortati si afisati lista generata la ex anterior. Stergeti numarul 0 folosind o functie. Afisati iar lista")

# lista_unita.sort() # sort sorteaza crescator, merge si pe litere
# lista_unita.remove(0)
# print(lista_unita)

print("5-7. aflati daca lista de la 3 este goala sau nu, goleste-o si verifica iar")

# lista_unita.clear()
# lista_unita.
# if len(lista_unita) == 0:
#     print("lista goala")
# else:
#     print(f"lista are {len(lista_unita)} elemente")

print("8-11. Ne jucam cu dict, afisam cheila si altele..")

# levi = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
# print(elevi.keys())
# print(f"Ana a luat nota {elevi["Ana"]}")
# elevi["Dorel"] = 6
# print(elevi["Dorel"])
# elevi.pop("Gigel")
# elevi["Ionel"] = 9
# print(elevi)

print("12. Set zile sapt si weekend, diferente, intersectie, uniune etc")

# zilele_saptamanii = {"luni", "marti", "miercuri", "joi", "vineri", "sambata", "duminica"}
# zilele_saptamanii.add("luni") # daca deja exista e doar odata
# weekend = {"sambata", "duminica"}
# print(zilele_saptamanii.union(weekend)) # cu unior le adunim nu merge cu add, aici irelevant
#
# if weekend.issubset(zilele_saptamanii.union(weekend)):
#     print("wekendul face parte din timpul saptamanii")
# else:
#     print("weekendul nu face parte")
#
# print(zilele_saptamanii.difference(weekend)) # arata care elemente din primul set nu sunt si in al doilea set
# print(weekend.difference(zilele_saptamanii)) # aici weekendul nu are nimic unic, si primesti set gol
# print(weekend.intersection(zilele_saptamanii))
# print(zilele_saptamanii.intersection(weekend)) # astea doua sunt clar la fel, arata doar elem comune


print("16. echipa de fotbal cu max 3 schimbari")

# echipa = ["adi", "barbu", "dan", "ion", "nicu"]
# schimbari_max = 3
# while True:
#     sch = input("pe cine schimbam ?")
#     if sch in echipa:
#         nou = input("pe cine trimitem?")
#         echipa.remove(sch)
#         echipa.append(nou)
#         schimbari_max -= 1
#         print(f"a intrat {nou} si a iesit {sch} mai aveti {schimbari_max} schimbari")
#         print(f' acum sunt in teren {echipa}')
#         if schimbari_max <= 0:
#             break
#     else:
#         print(f"nu se poate, jucatorul {sch} nu este in teren")
#         print(f"mai aveti {schimbari_max} scimbari")
# print("nu mai aveti schimbari disponibile, jucam asa")