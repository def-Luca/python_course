"recap_17"
lst = ["1", "2", "3"]

string = ""

# for x in lst:
#     if lst.index(x) == len(lst) - 1:
#         string += x
#     else:
#         string += x + "-"


"v2"
# for x in lst:
#     string += x +'-'
# string = string.strip("-")  # strip removes this char from the beggining and end
# # string = string[:-1]  # this slices the last char of the string

"v3"
for x in lst[:-1]:
    string += x + "-"
string += lst[-1]

print(string)

"v4"
# print("-".join(lst))  # join function(char to be used for joining, iterable)
print("-".join("abcdef"))  # works on a string also, it basically iterater through


"recap_18 iterate through two lists one of them in reverse order"
lst1 = [1, 2, 3, 4]
lst2 = [9, 8, 7, 6]

"v1"
# lst2 = list(reversed(lst2))  # reversing list 9
# for x in range(0, len(lst1)):  # we iterate the number of indeces
#     print(lst1[x], lst2[x])  # we print coresponding elements

"v2"
# for i in zip(lst1, reversed(lst2)):  # zip function binds according to index
#     print(i)

"recap_19 code return?"


def funct(a, b=22):  # returns a tuple
    c = "abc"
    return a, (b, c)


t, tt = funct(11)  #  first pos paramt then tuple gets assigned
print(t, tt)

"recap_20 code return?"

n = 100


def f():  # n in the function has local scope, doenst pop anywhere
    n = 45
    return n


f()  # to work we would have to assign global n to the function
print(n)  # this is referring to global parameter n which is 100


"recap_21 code return?"
lst = [5, 10, 15, 20, 25]
print(lst[::-2])  # negative step, beggins at the end, and steps with negative 2

