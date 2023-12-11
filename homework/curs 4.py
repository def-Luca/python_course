dictionar = {"a":{"aa":11, "ab":12}, "b":{"ba":{"bba":221}}, "c":{"ca": 31}}

dicte = {"a": 1, "b":2, "c":3}
print(dicte["a"])

print(dictionar["a"]["aa"])
print(dictionar.get("a").get("aa"))
print(dictionar.get("a")["aa"])
print(dictionar.get("b").get("ba").get("bba"))
print(dicte.get("d", "cheia nu exista"))   # asta e ce iti da daca nu gaseste

dict_nul = dicte.get("d", {})
dict_nul[0] = "marcel"
print(dict_nul)

#### CUrs 4

# mai_pot_o_tura = True
# while mai_pot_o_tura:
#     print("am mai alergat o tura")
#     mai_pot_o_tura = bool(int(input("mai poti o tura? 0 - nu, 1 - da")))


bul = 1     # 1 transf boolean true, 0 e fals
bul2 = ""    # string gol e flase in boolean
bul = bool(bul)
bul2 = bool(bul2)
print(bul)
print(bul2)

import random


dice_roll = 0 # aici poti sa incepi random
# while dice_roll != 3 and dice_roll != 6:

while dice_roll not in (3, 6):     # mai finut
    print(f" ai dat {dice_roll}, nu e 3 sau 6")
    dice_roll = random.randint(1,6)
    if dice_roll == 3 or dice_roll == 6:
        print(f" felicitari, ai dat {dice_roll}")

for i in range(0, random.randint(1, 6)):
    print(i)


# for se itereaza peste: collection si stringuri

for tura in range(5):
    print(f"tura {tura}")
    if tura == 4:
        print("inca putin")
        break
else:                            # ai esle si la for, se executa cnad se intrerupe, ajuta cand ai un break
    print(f"am alergat {5} ture")


dict = {"a": 1, "abcde": 2, "c" : 3, "d":4}

# for i in dict:                 # for in dict itereaza doar cheile
#      print(f"cheile dict sunt: {i}")
#      if dict[i] %2 ==0:
#          for j in i:
#              print(f"valorile cheilor cu val pare sunt {j}")


print(dict.items())  # facea tuple din element

for key, value in dict.items():   #cum iterezi doar prin valori simplu
    print(f"cu dict.items {key} {value}")
for key, value in enumerate(dict):   # functia asta iti da perechi de indexuri incepand cu 0
    print(f"cu enumerate {key} {value}")


lista = [i *2 for i in range(1,6)]   # list comprehension pt generare lista
print(lista)

# for i in lista:
#     print(f"elem {i} este in pozitia {lista.index(i)}")
#
# for i in enumerate(lista):    # enumerate e o functie care face tuple din index cu elemente
#     print(i)

for idx, elem in enumerate(lista):
    print(f"elem este {elem}, pe indexul {idx} ")

# limita = int(input("introd un nr "))
# lista = []
#
# for i in range(0, limita+1):
#  if i % 2 ==0:
#     lista.append(i)
# else:
#     print(lista)


# n = 15
#
# while n != 0:
#     print(n)
#     if n % 5 ==0:
#         n -=2
#
#     elif n % 2 ==0 and n>=3:
#         n -=3
#
#     else:
#         n-=1
# if n == 0:
#     print(0)
#
# #  break iesi din bucla
# n= 10
# while n in range(0,11):
#     print(n)
#     n -= 1
#     if n == 3:
#                  # asta nu mai lasa else sa se execute
#         print("3 e cu noroc")
#         break
# else:
#     print("while terminat")
# print(" de aici continua")


# continue
for x in range(1, 10):
    if x %2 ==0:
        continue    # cu continue sari peste nr pare
    print(x)

# pass # nu afecteaza codu, sa nu ne dea eroare uneori, tine loc de comanda

print("inainte")
for a in range(11):
    pass     # creez for dar nush la ce fol, scriu pass ca sa nu imi dea eroare
print("dupa")


animals = ["elefant", "girafa", "babuin", "zebra", "caine", "leu"]
indexat = {}

idx = -1
for i in animals:
    idx += 1
    if "e" not in i:
        continue
    indexat[i] = idx

print(indexat.keys())

#
#     indexat[idx] = i
#     idx +=1
# print(indexat)
#
# indexat["elefant"] = 0
# indexat[1] = "leu"
print(indexat)
