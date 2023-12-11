from exercitii.utilities import total_exercitii, exercitiu


exercitiu("Functie care sa calculeze si sa returneze suma a 2 numere")

# def suma (a, b):
#     return a+b
#
# print(suma(4, -6))

exercitiu(" Functie care sa returneze TRUE daca un numar este par, FALSE pt impar")

# def par_sau_impar(nr):
#     if nr % 2 == 0:
#         return True
#     else:
#         return False
#
# print (par_sau_impar(2.0))

exercitiu(
    """Functie care returneaza numarul total de caractere din numele tau complet.
(nume, prenume, nume_mijlociu) """
)

# def litere_nume(nume, prenume, nume_mijlociu):
#     x = len(nume) + len(prenume) + len(nume_mijlociu)
#     return x

# print(litere_nume("ioan", "luca", "marian"))

exercitiu("""" Functie care returneaza aria dreptunghiului""")

# def arie_dreptunghi(lungime, latime):
#     arie = lungime * latime
#     return arie
#
# print(arie_dreptunghi(20, 30))

exercitiu("""Functie care returneaza aria cercului""")
# import math
# print(f"pi este {math.pi}")
#
# def arie_cerc(raza):
#     arie = math.pi * raza**2
#     return arie
#
# print(arie_cerc(2))

exercitiu(
    "Functie care returneaza True daca un caracter x se gaseste intr-un string dat. Fasle daca nu"
)

# def finder(x, caracter):
#     if x.lower() in caracter.lower():
#         return True
#     else:    # daca nu pui else aici returneaza none
#         return False
#
# print(finder("k", "Luca"))


exercitiu(
    """Functie fara return, primeste un string si printeaza pe ecran:
Nr de caractere lower case este x
Nr de caractere upper case exte y 
"""
)

# def upper_lower_counter(word):
#     upper = []
#     lower = []
#     for i in word:
#         if i.isdigit():
#             continue
#         if i.isupper():
#             upper.append(i)
#         if i.islower():
#             lower.append(i)
#     print(f"sunt {len(lower)} litere mici si {len(upper)} litere mari ")
#
# upper_lower_counter("abCD 123")

exercitiu(
    "Functie care primeste o LISTA de numere si returneaza o LISTA doar cu numerele pozitive"
)

#

# def lista_pozitiva(*args):
#     nr_pozitive = []
#     for i in args:
#         if type(i) != int and float:
#             continue
#         if i>=0:
#             nr_pozitive.append(i)
#
#     return nr_pozitive

# print(lista_pozitiva(-2, 14, -66, 205, True, "tesla"))

exercitiu(
    """Functie care nu returneaza nimic. Primeste 2 numere si PRINTEAZA
Primul numar x este mai mare decat al doilea nr y
Al doilea nr y este mai mare decat primul nr x
Numerele sunt egal """
)

# def comparator(x, y):
#     if x>y:
#         print(f"{x} mai mare ca {y}")
#     elif y>x:
#         print(f"{y} mi mare ca {x}")
#     else:
#         print("numere egale")

# comparator(24, -15.7)

exercitiu(
    """Functie care primeste un numar si un set de numere.
Printeaza ‘am adaugat numarul nou in set’ + returneaza True
Sau Printeaza ‘nu am adaugat numarul in set. Acesta exista deja’ + returneaza False """
)

set = {x for x in range(10)}
# def number_in_set(x, set):
#     if x not in set:
#         set.add(x)
#         print(f"am adaugat numarul {x}in set")
#         return True
#     else:
#         print(f"{x} exista deja in set")
#         return False
#
# print(number_in_set(2.5, set))
# print(set)

exercitiu(
    """Functie care primeste o luna din an si returneaza cate zile are acea luna"""
)

# def zile_luna(luna):
#     luna = luna.lower()
#     if luna == "februarie":
#         return 28
#     elif luna in ["ianuarie", "martie", "mai" "iulie", "august", "octombrie", "decembrie"]:
#         return 31
#     else:
#         return 30
#
# print(zile_luna("octombrie"))

exercitiu(
    """Functie calculator care sa returneze 4 valori 
Suma, diferenta, inmultirea, impartirea a 2 numere"""
)

# def calcultaor (a, b):
#     suma =  a+b
#     scaderea = a-b
#     inmultirea = a*b
#     impartinrea = a/b
#     return suma, scaderea, inmultirea, impartinrea
#
# a, b, c, d = calcultaor(10, 2)
# print(a, b, c, d)

exercitiu(
    """Functie care primeste o lista de cifre (adica doar 0-9)
Ex: [1, 3, 1, 5, 9, 7, 7, 5, 5]
Returneaza un DICT care ne spune de cate ori apare fiecare cifra"""
)

# def dictionar (*args):
#     lista = list(args)
#     dict = {}
#     for x in range(10):
#         for y in lista:
#             dict[x] = lista.count(x)
#     print(lista)
#     print(dict)
#
# dictionar(2, 5, 2, 6, 2, 5)

exercitiu(
    """Functie care primeste 3 numere
Returneaza valoarea maxima dintre ele"""
)

# def greatest (*args):
#     return max(args)
#
# print(greatest(4, 2, 55, -12, 99, 20))

exercitiu(
    """Functie care sa primeasca un numar si sa retunreze suma tuturor numerelor de la 0 la acel numar"""
)

# def suma_pana_la(nr):
#     sum = 0
#     for x in range(nr):
#         print(x)
#         sum +=x
#     return sum
#
# print(suma_pana_la(22))

exercitiu(
    """ Functie care nu primeste argumente, dar cere un input de la tastatura si va printa
“Numarul ales este pozitiv” sau “Numarul ales este negativ” sau “Numarul ales este 0”, dupa caz, iar 
daca nu introducem un numar, sa se afiseze “Nu ati ales un numar valid”; 
# # la final sa se afiseze “Sfarsitul functiei” indiferent de caz."""
)
# def numar_valid ():
#     nr= input("introduceti un numar ")
#     try:
#         nr = float(nr)
#     except ValueError:
#         print("numar invalid")
#     else:
#         if nr == 0:
#             print("numaru e 0")
#         elif nr>0:
#             print("nr pozitiv")
#         else:
#             print("nr negativ")
#     finally:
#         print("sfarsitul functiei")
# #
#
# numar_valid()

exercitiu(
    """Functie care primesete 2 liste de numere (numerele pot fi dublate)
Returnati numerele comune """
)
#
# FOARTE CIUDAT CA FUNCTIA MERGE IN ALT FISIER #DEBUG
# def intersectie(a, b):
#     a = set(a)
#     b = set(b)
#     print(a.intersection(b))
#
# intersectie([x for x in range(8)], [x for x in range(3, 9)])


exercitiu(
    """Functie care sa aplice o reducere de pret. Daca apelul functiei nu primeste valoarea reducerii, sa ia valoarea default 10%.
Daca produsul costa 100 lei si aplicam reducere de 10%
Pretul va fi 90
Tratati cazurile in care reducerea e invalida. De ex o reducere de 110% e invalida"""
)


def reducere(pret, red=10):
    if red > 100 or red < 0:
        print("reducere invalida, pret nemodificat")
        return pret
    else:
        reducere = pret * red / 100
        pret = pret - reducere
        return pret


print(reducere(120, -75))

exercitiu(
    """Functie care sa afiseze data si ora curenta din ro
(bonus: afisati si data si ora curenta din China)"""
)

# from datetime import datetime
#
# now = datetime.now()
# current_time = now.strftime("%H:%M:%S")
# print(current_time)

exercitiu(
    """Functie care sa afiseze cate zile mai sunt pana la ziua ta / sau pana la craciun daca nu vrei sa ne zici cand e ziua ta :)"""
)


exercitiu(
    """ Functie care sa afiseze data si ora curenta din ro
(bonus: afisati si data si ora curenta din China)

20. Functie care sa afiseze cate zile mai sunt pana la ziua ta / sau pana la craciun daca nu vrei sa ne zici cand e ziua ta :)

21. Functie in care sa dai un nume romanesc si sa iti printeze pe ecran
‘Numele este de baiat’ sau ‘Numele este de fata’
"""
)
from datetime import datetime


today = datetime.today()
print(today)
