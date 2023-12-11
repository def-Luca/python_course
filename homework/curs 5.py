# data type numeric, boolean
# None e un missing value

a2 = None
print(type(a2))

my_string = "Luca"
#variabila =  valoare
# variabila are un loc in memorie unde e salvata

print(11//3)


my_text = "yes"
my_text+"something"
print(my_text + " of course")  # concatenare le lipeste intr un string

print(my_text * 3)  # multiplica stringul de n ori

lst = [12, 13] *10   # multiplica elem din lista
print(len(lst))
print(lst)


truth =  8> (3 and 6)
print(8> (3 and 6 ))

s1 = "str"
s2 = "substring"

print(s1 in s2)

import math

print (math.pi)

print(math.pi.__round__(3))  # cum faci round la un nr de digits

print(round(math.pi, 2))   # round rotunjeste in functie de decimale, echivalent metoda __round__?

a = True
b = True
c = False

print(not a or b and c)


hello = "Hello, World !"
print(hello[-1:-6:-1])

hello = hello.strip("!")   # scoti un caracter
lst = hello.split(" ", maxsplit=1)
print(lst)

x, y = lst    # poti sa faci unpacking la lista cu multiple assignment
print(x)

print(hello[1::3])

# string [start:stop:step]

