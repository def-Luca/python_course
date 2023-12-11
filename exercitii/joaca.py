print("nu e degeaba")
dicti = {}  # dont name a dict "dict" , iti blocheaza constructorul

dicti.update({"k": "v"})
dicti.update([(1, 2)])  # merge sa updatezi cu lista de tuple! neaparat lisita
print(dicti)
print(1 in dicti)

# presupunme ca astea sunt informatiile unei postari

post = {
    "user_id": 209,
    "message": "D5 E5 G5 F5",
    "language": "english",
    "datetime": "20230215T142",
    "location": (44.503, -104.2309320),
}

# mai creem un post folosind constructorul dict:

post2 = dict(message="SS Cotopaxi", language="english")
post2["user_id"] = 209  # asa adaugi un element in dictionar
post2["datetime"] = 1977116
print(post2)
print(post["message"])  # asa accesezi o valoare a unei chei

try:
    post2["location"]
except KeyError:
    print(" primesti KeyError daca nu avem cheia")
finally:
    print("ce solutii avem sa ne asiguram ca avem o cheie?")

# poti sa faci si cu if in...

print(dir(post2))  # dir metoda sa vezi ce metode avem
help(post2.get)  # asta nu returneaza, printeaza help direct

location = post2.get(
    "location", None
)  # cu get incerci sa iei val unei chei, daca nu are returneaza argument
print(location)

for key in post.keys():  # cum iterezi prin dict si iei si valorile
    value = post[key]
    print(key, "=", value)

for key, value in post.items():  # sau mai elegant cu .items care da tuple din elemente
    print(key, "=", value)
