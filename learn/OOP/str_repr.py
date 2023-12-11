""" if we just print the object of a class we get gibberish location
thats because class uses built in __repr__ function
which returns a hexadecimal id to the location of object in the memory
that is using the unless we define a __str__ method"""


class Ocean:
    def __init__(self, creature_name, creature_age):
        self.name = creature_name
        self.age = creature_age

    # __str__ has upper hand, if you just prin object you get the __str__ string
    def __str__(self):
        return f"creature {self.name} is {self.age} years old"

    # this is used more for programmers to gain info about object
    def __repr__(self):
        return f"Ocean : {self.name} : {self.age} "


c = Ocean("Jellyfish", 5)

print(repr(c))
print(c)  # same output, gibberish location
