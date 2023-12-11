from geo_shape_abstract import GeometricalShape

class Square(GeometricalShape):
    def __init__(self, side):
        self.__side = side

    def aria(self):
        return self.__side * 2

    def get_latura(self):
        print(f"latura este de {self.__side}")
        return self.__side

    def set_latura(self, new_side): 
        print(f"noua latura are {new_side}")
        self.__side = new_side

    def del_latura(self):
        print("patratul nu mai exista")
        self.__side = None


p1 = Square(4)

p1.descriere()

# acu joaca cu get set si delete
p1.set_latura(8)
p1.get_latura()
print(p1.aria())
p1.del_latura()
p1.get_latura()

class Circle(GeometricalShape):
    def __init__(self, radius):
        self.__radius = radius

    @property
    def radius (self):
        pass

    @radius.getter
    def radius(self):
        return f"radius is {self.__radius}"

    # poti sa ii pui si nume diferit
    # probabil mai finut sa il lasi la fel sa se simta ca un atirbut...

    @radius.setter
    def radius(self, new_radius:float):
        print(f"new radius is {new_radius}")
        self.__radius = new_radius

    @radius.deleter
    def radius(self):
        print("radius deleted")
        self.__radius = None


    def aria(self):
        return self.__radius **2 * self.PI


c1 = Circle(2)
c1.radius = 4
print(c1.radius)
print("new area is", c1.aria())

