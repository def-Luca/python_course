import unittest
"""exercises"""
def o_return(*args):
    o_list = []
    for o in args:
        if "o" in o.lower():
            o_list.append(o)
    return o_list


# now we use the TDD philosophy.
# first step is to def a function

# step nr 1 we define a function, pass it
# then write the test with the fail code

# step 2 write the function to pass the first test

# step 3 - refactoring write the function until it passes
def string_counter(string):
    lower_characters = 0
    upper_characters = 0
    for i in string:
        if i.isupper():
            upper_characters +=1
        else:
            lower_characters +=1
    return {"lower":lower_characters, "upper": upper_characters}
#
