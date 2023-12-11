"""abstraction is a way to control the inheritance
is like a constructor for classes
it also conceales the logic form the user
(you know what the function does and not how)
we have to import the ABC and abstractmethod"""
from abc import ABC, abstractmethod


class Car(ABC):  # our class inherit the ABC Class
    def description(self):
        print("it is a car")

    @abstractmethod  # we use abstractmethod decorator
    # we must have at least one abstractmethod for an abstract class!
    def model(self):
        pass
        # we can raise our own error here or just pass


class Dacia(Car):
    def model(self):  # here we define the abstract method
        print("dacia logan")


class Audi(Car):  # here we don't, we cant declare any object
    def culoare(self):
        print("audi red")


dacia = Dacia()  # this works fine
# audi = Audi()  # this will raise Type Error
dacia.description()
