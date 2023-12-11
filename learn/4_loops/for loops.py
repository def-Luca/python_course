"""for iterates through an interable object like string or list"""

for i in range(3, 10, 2):  # ranage (start, stop, step)
    print(i)
print("")
for i in range(10, -2, -2):  # last element -1 doesn't get iterated
    # if the step overlands the last element doesn't get iterated
    print(i)

x = [1, 2, 3, [1, 2]]
for i in x:  # list iteration
    print(i)

print("enumerate function")
# if we would want to loop throu list with indecees
s=0
for i in range(0, len(x)):
    print(f"element {x[i]} hast the index  {i}")
    s = s + i

#enumerate makes it easier
for i in enumerate(x):
    print(i)
for index, element in enumerate(x):
    print(f"element {element} has the index {index}")

# print("")
# s = "abcdef"
# for i in s:
#     if i == "a" or i == "b":
#         continue  # with continue you skip an iteration
#     print(i)
#     if i == "f":
#         print("i found an", i)
#         break  # with break you break the for loop
# else:  # here the else gets printed after for loop
#     print("found nothing")
#
#
# print("101 uneven dalmatians")
# # suppose we want to print the dalmatians with uneven number
# for i in range(1, 102, 2):
#     print("dalmatianul #", i)


print("")
# the count() method with the for loop
marimi  = [2, 3, 5, 3, 2, 4, 6, 2]
s=0
for i in marimi:
   if i==2:
       s += 1
print(f"element 2 is in the list {s} times")
