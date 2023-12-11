from abc import ABC, abstractmethod

class GeometricalShape(ABC):
    PI = 3.14

    @abstractmethod
    def aria(self):
        pass

    def descriere(self):
        print("I am probably pointy")

