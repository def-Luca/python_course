class Pet:  # we definde a parent class
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"my name is {self.name} and I am {self.age} years old")

    def speak(self):
        print("I don't speak!")


class Dog(Pet):
    # child Class Dog inherits from parent class Pet
    # we also get the constructor from the Pet class
    def speak(self):
        # we override the speak method form pet class, because dogs can bark
        print("Wof wof!")

    # here we also get the display method


class Cat(Pet):  # we define another child class
    def __init__(self, name, age, colour):
        # we can add other attributes like colour
        super().__init__(name, age)
        # this super() function gets the constructor from the parent class
        self.colour = colour

    def speak(self):
        print("Meow meow!")

    def display(self):
        print(f"my name is {self.name} and I am {self.age} years old and colour{self.colour}")


froggy = Pet("bubbles", 2)
doggy = Dog("rex", 5)
pussycat = Cat("lina", 6, "grey")


doggy.display()
doggy.speak()
froggy.speak()
pussycat.display()
