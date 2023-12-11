# permite obiectelor sa sa ia mai multe forme prin creearea unei interfete comune
# permite o agregare de clasa, ceva mai avansat...
"""allows methods and objects to take many shapes
through a common interface"""
class Romania:
    def language(self):
        print("romanian language")

class USA:
    def language(self):
        print("english language")

# we create a function as common interface for the two methods
def language_spoken(country):
    country.language()

r = Romania()
u = USA()

# as we iterate through elements every objects has a different return
for x in (r, u):
    language_spoken(x)

