"""dict = {"key": "value" (any type of data)}
they key hast tu be immutable
no order, values are accesed with key
as if a list has the key of the index"""

dictionary = {}  # we can declare an empty dictionary ! not a set

pupils = {"Sam": 10, "Bill": 8, "Joe": None}

pupils["Jill"] = False  # adding new element

print(len(pupils))  # shows the number of pair 'k':'v' in the dict
print(pupils["Sam"])  # print the value of the key, if not returns KeyError
print(pupils.get("Huehl", "No Huehl in the class!"))
# returns value of the key, if not returns default None, or the second argument

pupils["Bill"] = 9  # we can override the value of a key
del pupils["Joe"]  # del operator deletes a pair based on the key
print(pupils)


pop = pupils.pop("Sam")  # deleting a pair and returns it to a variable
print(pupils, pop)

pupils_2 = {"Lupu": 9.5, "Olteanu": 8}

pupils.update(pupils_2)  # similar to append for lists
pupils.update([("Elisa", "8"), ("Miuta", 4)])  # or with a list containing tuples
print(pupils)
print(pupils.keys())  # returns just the keys

print(pupils.items())  # creates a tuple for each ("k", "v")
# useful for iterating through the pairs with for
for x in pupils.items():
    print(x)
for y in pupils:  # for iterates only through keys
    print(y)

pupils.clear()  # deletes all the elements
print(pupils)  # and you get an empty dict
