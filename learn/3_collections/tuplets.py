# tuples are an ordently, fixed, immutable collection of data
# we declare tuples with round brackets
# immutable means they cant be changed after declaration with append or insert
# they can contain mutable objects

tupl = (1, 4, 2, True, (1, 2), [3, 4])

tupl[-1][1] = "list"  # the list being mutable i can change inside the tuple
print(f"tuple length is {len(tupl)} elements")
print(tupl[4])  # acces the index
tupl = list(tupl)  # making the tuple a list
tupl.append("haha")  # then appending
tupl = tuple(tupl)  # then tuple again


# same as above with a function
def tuple_append(tupl, new_element):
    tupl = list(tupl)
    tupl.append(new_element)
    return tupl


print(tuple_append(tupl, "element_from_function"))

# we can extend a list with a tuple
fruits = ["apple", "banana"]
fruits.extend(tupl)
print(fruits)
