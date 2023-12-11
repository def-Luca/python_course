from encapsulation import Person
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def show(self):
#             print(f"{self.name} is {self.age} years old")
#
#     # we override the __str__method
#     def __str__(self):
#         return(f"{self.name} is {self.age} years old")

class Employee(Person):
    def __init__(self, name, age, hourly, number_of_hours):
        super().__init__(name, age)
        # same super() init function with other syntax
        # Person.__init__(self, name, age)
        self. hourly = float(hourly)
        self.number_of_hours = int(number_of_hours)

    def show_finance(self):
        print(f" {self.name} earns monthly {self.hourly * self.number_of_hours * 4}")

employee = Employee("Luca", 26, 18, 40)
employee.show()
employee.show_finance()

