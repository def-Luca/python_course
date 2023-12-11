class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def area_rectangle(self):
        return self.width * self.length

    def display(self, caracter="*"):
        for i in range(self.width):
            print(caracter * self.length)
