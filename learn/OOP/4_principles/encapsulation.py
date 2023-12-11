"""Encapsulation helps us conceal the attributes from the user
we can access this private attributes with methods within the class
Private attribute syntax: __attribute
    private can't be called outside the class!
Protected attribute syntax: -attribute
    protected can be called outside the class we usually don't
    protected can't be imported
"""

class Computer:
    __GLOBAL = 10  # private global attribute


    def __init__(self):
        self.__price = 1000  # privat local attribute
        self._cpu = "intel"

# we need a method to get acces to the attributes
    def change_price(self, price):
        self.__price = price

    def show_price(self):
            print(self.__price)

    # you can also create a hidden function
    def __hidden__(self):
        print(f"hidden variable is {self.__GLOBAL}")

    # and create another function to call it
    def call_hidden(self):
        self.__hidden__()

#accesezi atributul
c1 = Computer()
print(c1._cpu)  # we can call the protected attribute
# print(c1.__price)  # raise AttributeError

c1.change_price(1500)  # we change the private attribute with the method (setter)
c1.show_price()  # and we access it also with the metod (getter)
# c1.__hidden()  # here also AttributeError
c1.call_hidden()  # we call the private method with the other method


# how to display objects in the class only with print
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
            print(f"{self.name} is {self.age} years old")

    # we override the __str__method
    def __str__(self):
        return(f"{self.name} is {self.age} years old")


p1 = Person("John", 20)

p1.show()
print(p1)  # prin metoda __str__
# normally you get object at gibberish location




