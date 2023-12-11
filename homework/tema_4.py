import random

print("1. lista cu masini si interatii")

masini = ['Audi', 'Volvo', 'Bmw', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']

# for masina in masini:
#     print(f"masina mea preferata este {masina}")
#
# iter = 0
# while iter <= len(masini)-1:
#     print(f"masina mea preferata este {masini[iter]}")
#     iter +=1
# # acelasi lucru cu while, ceva mai complicat

# for idx, masina in enumerate(masini):
#     print(f"masina mea preferata {masina} este in pozitia {idx}")


print("2. for in for cu capitalizare")
#
# for masina in masini:
#     for l in masina:
#         print(l)

# for i in range(len(masini)):
#     print(i)
#     if i == 0 or i == (len(masini)-1):
#         masini[i] = masini[i].lower()
#     else:
#         masini[i] = masini[i].upper()
# print(masini)



# t = 0
# for masina in masini:
#     for n in masina:
#         print(n)
#         print(type(n))

# for t in masini:
#     t = t[0].lower() + t[1:len(t) - 1].upper() + t[-1].lower()
#     print(t)

# fucking wild

print("3. cineva cumpara mercedesul")

# masina_dorita = input("ce masina doriti sa cumparati? ").capitalize()
# for masina in masini:
#     if masina == masina_dorita:
#         masini.remove(masina_dorita)
#         print(f"am gasit masina dorita de dvs, un {masina_dorita}")
#         print(f"au ramas acum numai {masini}")
#         break
#     else:
#         print(f"avem un {masina} , nu e buna")

print("4. vine unu bogat si nu vrea sa vada trabant si lastun")

# for masina in masini:
#     if masina == "Trabant" or masina == "Lastun":
#         continue
#     else:
#         print(f"avem pentru dvs un {masina}")

print("5. modernizam parcul auto prin programul rabla")

masini_vechi = []
# for masina in masini:
#     if masina.capitalize() == "Trabant" or masina == "Lastun":
#         masini_vechi.append(masina)
#         masini[masini.index(masina)] = "Tesla"

# for i, m in enumerate(masini):
#     if m.lower() == "trabant" or m.lower() == "lastun":
#         masini_vechi.append(m)
#         masini[i] = "Tesla"
#
# print(masini)
# print(masini_vechi)

print("6. dict cu masini si cumparare")

# pret_masini = {"Dacia":6800 , "Lastun":500, "Opel":1100, "Audi":19000 , "BMW":23000}
# buget = 15000
#
# for masina in pret_masini:
#     pret = pret_masini[masina]
#     if pret > buget:
#         continue
#     else:
#         print(f"avem masina {masina} la pretul {pret}")

print("7. lista de numere si joaca")

lista = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
print(lista)
# trei=0
# for nr in lista:
#     if nr == 3:
#         trei +=1
#         print("am gasit un 3")
# print(f"avem {trei} de 3")
#
# sum = 0
# for nr in lista:
#     print(nr)
#     if type(nr) == int:
#         sum +=nr
# print(f"suma numerelor este {sum}")

# nr_mare = 0
#
# for nr in lista:
#     print(nr)
#     if nr > nr_mare:
#         nr_mare = nr
# print(f"cel mai mare numar este {nr_mare}")

# for nr in lista:
#     if nr >0:
#         lista[lista.index(nr)] =-abs(nr)
#     if nr <0:
#         lista[lista.index(nr)] = abs(nr)
#
# print(lista)

#furmos finut cu enumerate
#for x, y in enumerate(lista):
#     if y>0:
#         lista[x] = -y

#sau mai superb cu comprehension

# print([-abs(x) for x in lista])


print("11 mutam elemente din liste")

lista = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]

# numere_pare = []
# numere_impare = []
# numere_pozitive = []
# numere_negative = []
#
# for nr in lista:
#     if nr > 0:
#         numere_pozitive.append(nr)
#     if nr < 0:
#         numere_negative.append(nr)
#     if nr % 2 ==0:
#         numere_pare.append(nr)
#     if nr % 2 != 0:
#         numere_impare.append(nr)
#
# print(numere_pozitive)
# print(numere_negative)
# print(numere_pare)
# print(numere_impare)


print("Aceeasi lista. Ordonati crescator lista fara sa folositi sort")

# print(lista)
#
# l1 = []
# n = int(input("cate cifre sa aiba lista? "))
#
# for i in range(0, n):
#     elem = int(input(f"introduceti cifra nr. {i+1}"))
#     l1.append(elem)
#
# print(l1)
#
# for x in range(0, len(l1)):
#     for y in range(x+1, len(l1)):
#         if l1[x]> l1[y]:
#             l1[x], l1[y] = l1[y], l1[x]
#
# print(f"lista ordonata crescator este{l1}")

print("------------------")

print("ghicitoare numar")

# numar_secret =  random.randint(1, 31)
#
# while True:
#     numar_ghicit = int(input("care e numarul"))
#     if numar_ghicit == numar_secret:
#         print("ai ghicit, era", numar_secret)
#         break
#     elif numar_ghicit < numar_secret:
#         print("numarul este mai mare")
#     else:
#         print("numarl este mai mic")

print("piramida de numere")

# int = int(input("introduceti un numar pentru piramida"))
# cheie = 1
#
# while int>=cheie:
#     print(str(cheie) * cheie)
#     cheie +=1

tastatura_telefon = [[1,2,3],[4,5,6],[7,8,9],[0]]

for l in tastatura_telefon:
    for m in l:
        print(m)

for l in tastatura_telefon[1]:
    print(l)

