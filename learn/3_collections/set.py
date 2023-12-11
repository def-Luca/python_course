"""Sets are a collection of elements without order or frequency
they can only contain imutable objects (no list or dicts)
they are faster than lists
we use when we care only if something exists or not"""

# we declare it using brackets, same as dicts, but without keys
x = {1, 2, 3, 4, 2, 5}
y = {2, 4, 6, 8}

s3 = {1, 2, 3}
s2 = {1, 3, 2}
print(s2 == s3)  # True because there is no order

x.add("11")  # add method adds a value
x.remove(5)  # remove method removes an element
print(4 in x)  # in operator to check if an element is there
print(x)

# sets operation
print("union")
# Union means the sum of the sets, functino union or symbol "|"
print(x.union(y))  # intersectia, le aduna
print(x | y)

print("Intersection")
# That means only the common elements, functino intersection or symbol "&":
print(y.intersection(x))
print(x & y)

print("Difference")
# That means only the different elements, function difference or symbol "-":
print(x.difference(y))  # which elements from x are different from y
print(x - y)
print(y.difference(x))  # here order matters!
print(y - x)

print("Symmetric difference")
# basically a new set without common elements, order doesn't matter
print(x.symmetric_difference(y))
print(y.symmetric_difference(x))
print(x ^ y)

# We can convert a list into a set to delete the duplicates
print("Eliminate duplicates using list to set")
lista = [1, 1, 2, 2, 3, 4, 5, 1]
lista = list(set(lista))
print(lista)

