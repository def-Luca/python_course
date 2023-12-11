class Car:
    # fields - this will automatically be attached to the object created
    mark = "Mercedes"
    model = None  # you can delcare it with None
    release_year = 2022
    licensed = False
    colour = None

    def __init__(self, var_model, var_culoare, var_leather=False):
        self.model = var_model
        self.colour = var_culoare
        self.leather = var_leather  # create attribute from constructor

    # methods
    def paint(self, var_culoare):
        self.colour = var_culoare

    def accelerate(self):
        print("Vruuum!")

    def brake(self):
        print("Scaaaartz!")

    def licence(self):
        self.licensed = True

    def electric_windows(self):
        # method that creates another atribute
        self.windows = True


car = Car("EQS", "white")
car.electric_windows()
print(car.windows)
