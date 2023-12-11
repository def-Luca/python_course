# exersam listele


lista = []
lista2 = [0 for _ in range(0, 2)]
dict = {"k" : "v"}
print(type(dict))
tuplu = ()
print(type(tuplu))
set = {1}
print(type(set))

lista.append(1)
lista.append(0)
lista.append(3)
lista.append(5)
lista.insert(1, 2)
lista.append(int(str(6)))
print(lista.index(2))
lista.extend(lista2)  # e un fel de append pentur iterabile
lista.extend(dict) # aici extinde doar cu cheile dictului
lista.remove(0)  # remove ia valori
pop = lista.pop(1) # aici ia index si returneaza
print(pop)
lista.remove("k")
lista.sort()  # sorteaza lista de int sau float crescator
lista.reverse() # inverseaza lista nu are trb cu ordonarea
lista.count(0) # nr de cate ori apare o valoare intr o lista
lista3 = lista.copy() # cum copiezi o lista are return
lista.clear() # am sters lista 2, ramane lista 3
lista3 = lista3.__add__([lista2]) # functia add da return!
print(lista3.index(lista2))
lista3.__init__([-1, -2]) # initializeaza o lista, nu imi dau seama de ce mai smq

lista3.extend([4, 2, 3, 1])
lista3.sort()

lista3[lista3.index(1)] = (5, 8, 12)

lista_slice = lista3[::-1]




print(lista)
print(len(lista2))
print(lista3)
print(lista_slice)
