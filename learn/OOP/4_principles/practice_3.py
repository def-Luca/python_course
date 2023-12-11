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


class Student(Person):
    def __init__(self, surname, age, grade, scholarship):
        super().__init__(surname, age)
        self.grade = grade
        self.scholarship = scholarship

    def show_finance(self):
        return self.scholarship


s1 = Student("Luca", 26, 10, 1000)
print(s1.show_finance())

s2 = Student("Miha", 25, 9, 900)
s1.show()
s2.show()
