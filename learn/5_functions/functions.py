"""Functions means a logic that we can declare
and reuse it many more times
def function(parameters):
    command_to_execute
function(arguments) to call the function
Implicit functions in python like print(), extend()...
Defined functions liek the ones we write
"""
name = "Ioan"  # this you call global argument, or global purpose


# the simplest function ever
def greeting():
    print("Greetings")


greeting()  # we call the function with brackets


# here we have a function with parameters
# we rewrite the previous function
def greeting(name, surname):
    name = name.capitalize()
    surname = surname.capitalize()
    print(f"Hello {name} {surname} ")


greeting("Luca", "Ioan")
# when we call the function we give arguments!

"""return ends a function and
returns gives the result, so we can pass it further
return functions are in generale more flexible
we can define a variable as optional by giving a default
optional parameters are always last
love child of break and .pop"""

# for example sorted() function and .sort method
lst = [4, 2, 7, 3, 6, 2, 9]
sorted(lst)  # sorted() function sorts and returns, doesn't modify the object
print(lst)

lst.sort()  # .sort() method modifies the object but doesn't return
print(lst)


# function to determine whether somebody is of legal age:
def major(age):
    if age >= 18:
        return True
    else:
        return False


print(major(18))

"""if no arguments passed, default one will de used
 as if you override the optional argument
the number word as parameter only exists inside of the function
that we call local purpose
here is a function to add the arguments"""


def greeting(surname, greeting = "Greetings"):  # these variables have local purpose
    global name  # we use the word global to refer to the global argument
    print(f"{greeting} {name} {surname}")


greeting("Mihaela", "Good Day")

"""there are functions with multiple arguments, called *args
these are passed and seen as a tuple"""


def multiply(*number):
    return number


x = multiply(2, 3, 4, "6")
print(x)
print(type(x))


def sum(*numar):
    total = 0
    for x in numar:  # we iterate through the tuple with *args
        total += x
    return total


tupl = (1, 2, 5, 2.5)
x = sum(1, 2, 5, 2.5)
y = sum(*tupl)  # if we pass a tuple we MUST add "*"
print(x)
print(type(x))
print(y)

"""We can also create a function dealing with dictionaries
these are callled **kwargs (key word arguments)
these function sees the arguments as a dictionary
syntax a bit different when passing the **kwargs!
**kwargs are not passed with quotation marks
def function(key="value", key1 = value 2)
dict = {"key":"value}"""


def country_population(**kwargs):
    population = 0
    for c in kwargs:
        population += kwargs[c]
    return population


# if you provide dict as argument, you have to speecify with "**" that is a kwarg
countries = {"romania": 19_500_000, "germany": 83_000_000, "india": 1_400_000_000}
x = country_population(romania=19_500_000, germany=83_000_000, india=1_400_000_000)
y = country_population(**countries)  # don't forget about **kwargs
print(x)
print(y)


# here we use *args with optional parameter
def largest(*args, greatest=100):
    if max(args) < greatest:
        return greatest
    return max(args)


# we have to specify optional_argument = value
g = largest(55, 24, 55, greatest=30)
print(g)

""" Some syntax rules
syntax is def function (positional_param, optional_parameter, *args, **kwargs)
after **kwargs comes no other parameter
optional parameter sits after  positional one
optional parameter can sit before or after *args"""
