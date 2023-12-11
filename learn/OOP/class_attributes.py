class Person:
    NUMBER_OF_PERSONS = 0  # this is a class attribute
    # they are used generally to store constants

    @classmethod  # decorator for a class method
    def number_of_persons(cls):  # we use the cls word
        return cls.NUMBER_OF_PERSONS()  # acts on the class itself

    # they don't act on the class objects!
    @classmethod
    def increase_persons(cls):
        cls.NUMBER_OF_PERSONS += 1

    def __init__(self, name):
        # each object will have a different name
        self.name = name
        Person.increase_persons()  # here we call the class method


# each instantieted object will add a 1 to the class attribute
p1 = Person("Jim")
p2 = Person("Tim")
p3 = Person("Joe")
p1.increase_persons()  # here we increase the number from the method
print(p2.NUMBER_OF_PERSONS)
