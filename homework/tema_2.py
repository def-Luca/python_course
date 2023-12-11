print("2. Verificati si afisati daca x este numar natural sau nu")
# x = float(input("introduceti un numar"))
# if x<0:
#     print("numarul este negativ")
# elif not x.is_integer() == True:
#     print("numarul nu este natural")
# else:
#     print("numarul este natural")


print("3.Verificati si afisati daca x este numar pozitiv, negativ sau neutru")
# nr = int(input("introduceti un numar"))
# if nr<0:
#     print("numarul este negativ")
# elif nr>0:
#     print("numarul este pozitiv")
# elif nr==0:
#     print("numarul este neutru")

print("ex4. Verificati si afisati daca x este intre -2 si 13")
#
# r = int(input("introduceti un numar"))
# if r < -2 or r>13:
#     print("numar mai mic decat -2 si mai mare decat 13")
# else:
#     print('numar intre -2 si 13')

print("ex.5 Verificati si afisati daca diferenta dintre x si y este mai mica de 5")

# x, y = input("introduceti 2 numere").split()
# x, y = int(x), int(y)
# print(x, y)
# print(type(x), type(y))
# z =  abs(x-y)
# print(z)
# if z < 5:
#     print("diferenta este mai mica de 5")
# else:
#     print("diferenta e prea mare")

print("ex.6 Verificati daca x NU este intre 5 si 27. (a se folosi ‘not’)")

# x = int(input("introduceti un numar"))
# if not(5<=x<=27):
#     print("numarul nu este intre 5 si 27")

print('ex.7.x si y (int) Verificati si afisati daca sunt egale, daca nu afisati care din ele este mai mare')
# x = float(input('introduceti primul numar'))
# y = float(input("introduceti introduceti al doilea numar"))
# if x.is_integer():
#     x = int(x)
# if y.is_integer():
#     y = int(y)
# if x==y:
#     print("numerele sunt egale")
# elif x > y:
#     print(f"{x} este mai mare decat {y} cu {x-y} unitati")
# elif y>x:
#     print(f"{y} este mai mare decat {x} cu {y-x} unitati")
# else:
#     print("eroare")

print("8. X, y, z - laturile unui triunghi, Afisati daca triunghiul este isoscel, echilateral sau oarecare.")

# x = float(input("introduceti latura unui triunghi"))
# y = float(input("introduceti latura unui triunghi"))
# z = float(input("introduceti latura unui triunghi"))
#
# if x==y==z:
#     print("triunghiul este echilateral")
# elif x== y or x==z or y==z:
#     print("triunghiul este isoscel")
# else:
#     print("triunghiul este oarecare")

print("9. Cititi o litera de la tastatura. Verificati si afisati daca este vocala sau nu")

# litera = input("introduceti o litera").lower()
# vocale = ["a", "e", "i", "o", "u"]
# print(litera)
# print(vocale)
# if len(litera)>1:
#     print("mai mult de un caracter introdus")
# else:
#     if vocale.count(litera)>0:
#      print("litera este o vocala")
#     else:
#         print("litera este o consoana")

print("10. Transformati si printati notele din sistem romanesc in  > note Americane")

# nota = float(input("introduceti nota obtinuta"))
# nota = int(nota)
# note_america = {10: "A", 9: "B", 8:"C",7:"D", 6:"E", 5:"E", 4:"F", 3:"F", 2:"F", 1:"F" }
# print(note_america)
# if nota>10 or nota<1:
#     print("nota invalida")
# else:
#     print(f"ai luat in america nota {note_america[nota]}")

print("ex.11. .Verificati daca x are minim 4 cifre (x e int)")

# cifre = abs(int(input("introduceti in numar")))
# cifre = str(cifre)
# if cifre.isdigit() == True:
#     if  len(cifre) >=4:
#         print(f"numarul are {len(cifre)} cifre")
#     else:
#         print("numarul are mai putin de 4 cifre")
# else:
#     print("nu e numar")

print("12. Verificati daca x are exact 6 cifre ")

# exact = input("introduceti un numar")
# if exact.isdigit() == False:
#     print("nu este numar")
# else:
#     if len(exact) == 6:
#         print(f" {exact} are exact 6 cifre")
#     else:
#         print("nr nu are fix 6 cifre")

print("13. Verificati daca x este numar par sau impar x e int")

# par = abs(int(input("introduceti un numar")))
# par = int(par)
# if par % 2== 0:
#     print(f"{par} este un numar par")
# else:
#     print(f"{par} este un numar impar")

print("14. Afisati care este cel mai mare dintre ele?")

# x = 8
# y = 2
# z = 9
# a = 2
# b = 11
#
# tuple = (x, y, z, a, b)
# c = tuple[0]
# for i in tuple:
#     if i>c:
#         c = i
# else:
#     print(c)

print("ex15. X, y, z - reprezinta unghiurile unui triunghi. Verificati si afisati daca triunghiul este valid sau nu")

# x = input("introduceti primul unghi al unui triunghi")
# if x.isdigit():
#     x = int(x)
# else:
#     print("gresit ai peirdut")
#     quit()
# y = input("introduceti al 2-lea unghi al unui triunghi")
# if y.isdigit():
#     y = int(y)
# else:
#     print("gresit ai peirdut")
#     quit()
# z = input("introduceti al 3-lea unghi al unui triunghi")
# if z.isdigit():
#     z = int(z)
# else:
#     print("gresit ai peirdut")
#     quit()
# if x+y+z != 180:
#     print("unghiurile nu sunt valide")
# else:
#     if x == y == z:
#         print("triunghiul este echilateral")
#     elif x== y or x==z or y==z:
#         print("triunghiul este isoscel")
#     else:
#         print("triunghiul este oarecare")

print('''14. Avand stringul: 'Coral is either the stupidest animal or the smartest rock'.
Cititi de la tastatura un int x.
Afisati stringul fara ultimele x caractere.
ex: daca ati ales 7 => 'Coral is either the stupidest animal or the smarte''')

# string = 'Coral is either the stupidest animal or the smartest rock'
#
# while True:
#     excl = input ("introdu cate caractere de la final sa tai")
#     if excl.isdigit():
#         excl = int(excl)
#         if excl >= len(string):
#             continue
#
#         break
#
# print(f" propozitia fara ultimele cifre este: {string[0:len(string)-excl]}")
# print(f"caracterele excluse sunt {string[len(string)-excl:len(string)]}")

print("17. Acelasi string.Declarati un string nou care sa fie format din primele 5 caractere + ultimele 5")

# string = ("Coral is either the stupidest animal or the smartest rock")
# string_nou = string[0:6] + string[len(string)-5: len(string)+1]
# print(string_nou)
# print(string[-1])

print('''18. Acelasi string.
Salvati intr-o variabila si afiseaza indexul de start al cuvantului rock.
(hint: este o functie care va ajuta sa faceti asta).
Folosind aceasta variabila + slicing, afisati tot stringul pana la acest cuvant.
output: 'Coral is either the stupidest animal or the smartest ''')

# string = ("Coral is either the stupidest animal or the smartest rock")
# i = string.find("rock")
# print(string[0:i])

print('''Cititi de la tastatura un string.
Verificati daca primul si ultimul caracter sunt la fel.
Se va folosi un assert.
Atentie: se doreste ca programul sa fie case insensitive ''')

# while True:
#     cuvant = input("introduceti o propozitie").lower()
#     if cuvant[0] == cuvant[len(cuvant)-1]:
#         print("primu si ultimu caracter sunt la fel")
#         break
#     else:
#         print("you fail, once again")

print('''20. Avand stringul '0123456789'
Afisati doar numerele pare 
Apoi afisati doar numerele impare
(hint: folositi slicing, controlati din pas) ''')
#
# numar = "0123456789444578666332"
# print(numar[0:len(numar)-1:2])
# print(numar[1:len(numar)-1:2])
#
# numere_pare = ""
# numere_impare = ""
# for i in numar:
#     i = int(i)
#     if i %2 ==0:
#         i = str(i)
#         numere_pare = numere_pare+i
#     elif i%2 != 0:
#         i =str(i)
#         numere_impare = numere_impare + i
# print(numere_pare)
# print(numere_impare)


print("21. imbarcare persoane")
#
# DA = "bine ati venit la bord"
# NU = "ne pare rau, nu va puteti imbarca"
#
# while True:
#     varsta = input("introduceti varsta")
#     if varsta.isdigit():
#         varsta = int(varsta)
#         if varsta >=18:
#             pasaport = input("aveti pasaportul?").lower()
#             if pasaport == "da":
#                 print(DA)
#                 break
#             else:
#                 print(NU)
#                 break
#         else:
#             parinti = input("sunteti insotit de ambii parinti?").lower()
#             if parinti == "da":
#                 print(DA)
#                 break
#             else:
#                 parinte = input("este macar unul din parinti prezent?").lower()
#                 if parinte == "da":
#                     permisiune = input("celalalt parinte si a dat permisiunea?").lower()
#                     if permisiune == "da":
#                         print(DA)
#                         break
#                     else:
#                         print(NU)
#                         break
#                 else:
#                     print(NU)
#                     break
#
#
#     else:
#         print("date invalide, incercati din nou")
#
# print("va mai asteptam")

print("22. joc de ghicit zarul")
#
# import random
# while True:
#     dice_roll = (random.randint(1, 6))
#     numar = input("ghiciti numarul zarului")
#     if numar.isdigit():
#         numar = int(numar)
#         if numar <1 or numar>6:
#             print("false input, again")
#         else:
#             if numar == dice_roll:
#                 print(f"Corect, ai ales {numar} si zarul a fost {dice_roll}")
#                 break
#             elif numar > dice_roll:
#                 print ("numarul este mai mic, mai incearca")
#             else:
#                 print("numarul este mai mare, mai incearca")
#     else:
#         print("false input, again")
#
# print("O zi buna!")

###### din tema:
# la ex 1 f interesant:
#
# x = 3.5
# if x >= 0 and isinstance(x, int):   #functia iti zica daca primu argument e de un tip anume
#     print("numarul este natural")
# else:
#     print("nr nu e natural")


### la ex 2 iar blana, cu functie in range:

# x = float(input("ia zi varule un nr"))
# if x in range(-2, 14, 0.1):       # buna idee, dar nu mere cu float cu virgula ca range da nr natural
#     print(True)
# else:
#     print("fals")

# litera = input("introduceti o litera").lower()
# vocale = {"a", "e", "i", "o", "u" }  # cu set mai elegant, mai easy pt procesor
# print(litera)
# print(vocale)
# if len(litera)>1:
#     print("mai mult de un caracter introdus")
# else:
#     if litera in vocale:
#         print("litera este o vocala")
#     else:
#         print("litera este o consoana")


# x = float(input("baga"))
# x = str(x).replace(".", "")
# x = str(x).replace("-", "")
# if len(x) == 6:
#     print(f"{x} are exact 6 cifre")
# else:
#     print("nu are 6 cifre")