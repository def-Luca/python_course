"""
comments are made with hashtag sign for one line
or with 3 quotation marks
"""
# a variable is place from memory of a computer which stores one value
# a variable name can't have blank spaces, we use underscore
# declaring a variable is made using equal sign

name = "John Smith"  # variable name has value "John Smith"
name = "Peter Pan"  # variable can be overwritten
print(name)

"""
you can declare multiple variables in one line
or the same value to multiple variables
"""

sex, size = "masculin", 1.70
hair_colour = eye_colour = "negru"
print(eye_colour)
print("-----------------------")
print(type(hair_colour))
# type function shows which type of data is stored in the variable

# type casting for changing the variable type
"""
int()
str()
float()
bool()
"""

shoe_size = "42"
shoe_size = int(shoe_size)  # use the appropriate function
print(type(shoe_size))
print("----------------")

# how to interchange two variables
# difficult way
x = "number"
y = 10
change_variable = (x, y)
x = change_variable[1]
y = change_variable[0]
print(x, y)

# the easy pythonian way
a = 12
b = "cheese"
a, b = b, a  # tuple unpacking, behind  there are two tuple created
print(a, b)
