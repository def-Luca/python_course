# aparent s a sters, tragic, reiau de la curs


a = 2
b = 2
c = a
print(a is b)  # is verifica daca sunt stocate in acelasi loc in memorie
print(b is c)
print(id(a))  # cu id verifici locatia din memorie unde sunt stocare variabilele
print(id(b))
print(id(c))


s1 = "abc"
s2 = "xyz"

print(s1 > s1)
print(
    ord(s1[0]), ord(s2[0])
)  # compara pe rand ordinalele substrigurilor, x(120) e mai mare ca a (97)


alfa = "abcdefghijklmnopqrstuvwxyz"
for i in alfa:
    print(ord(i))  # deci si literele sunt ordonate in ordinale

# operatorul in si not in

a = "apple"
print("a" in a)  # verifica daca substringul este intr un alt string sau element

lista = [1, 2, 3, 44, [1, 2, 3], "apple"]
print(44 in lista)  # trebuie sa fie un element intreg la lista
print(a not in lista)

# exercitiu

string = input("introd")

string_nou = string[0] + string[len(string) // 2] + string[-1]

print(string_nou)
