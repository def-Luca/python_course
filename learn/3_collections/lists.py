"""List are an orderly collection of any elements,
they are mutable (can be modified) and dynamic,
they are declare by square brackets"""

empty_list = []  # you can declare an empty list
fruits = ["apple", "apple", "orange", 3, True, 3]

print(fruits)  #
print(fruits[1])  # you can access elements by indexing them
print(fruits[-1])  # just like a string
fruits[1] = "banana"  # overriding an element

fruits.append("tomato")  # append adds at the end of the list
fruits.insert(0, "kiwi")  # insert at index..., element....
print(fruits)

print(f"the list has {len(fruits)} elements")  # len returns number of elements as int

last_element = fruits.pop()
# pop deletes last element and returns it
print(last_element)
print(fruits.pop(-1))
print(fruits)

print(f"we have element 3 {fruits.count(3)} times in the list")
# counting the number of an element in a list

exotic_fruits = ["ananas", "mango"]
fruits.extend(exotic_fruits)  # extend combines lists
# append would have appended the list to the list
print(fruits)

print("")  # just seems nicer format when printed
print("combining lists")

numbers = ["a", "b", 3, [1, 2, 3], (4, 5, 6)]  # lists can contain other lists also
print(numbers[3])
x = numbers[3]
print(x[2])  # acces elem index 2 form the list in the list
if len(numbers[3]) == 3:
    print("list has 3 elements")
else:
    print("list doesn't have 3 elemnts")

numbers.append(None)  # you can append None element
numbers.insert(1, "26")
numbers[1] = "25"
numbers.append("a")
numbers.remove("b")
numbers.remove("a") # it removes the first element
print(numbers.index("a"))  # returns first index of a value
print(numbers)

numbers = [1, 2, 5, 1, 23, 123]  # overriding the list
print(sorted(numbers))  # returns a sorted list, doesn't override the original

# delcaring a list with comprehension
lista = [x for x in range(3)]  # initializare lista cu for
print(lista)
