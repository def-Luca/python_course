"""objects of two different classes can interact with one another"""


class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade


class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.maxim = max_students
        self.student_list = []

    def add_student(self, student):
        if len(self.student_list) < self.maxim:
            self.student_list.append(student)
            return True
        else:
            print("no more places")

    def show_average(self):
        value = 0
        for student in self.student_list:
            value += student.grade
        return value / len(self.student_list)


s1 = Student("Luca", 26, 10)
s2 = Student("Mihaela", 25, 9)
s3 = Student("Vlad", 23, 8)

course1 = Course("it", 2)
course2 = Course("medicine", 3)

course1.add_student(s1)
course1.add_student(s2)
print(course1.student_list[0].name)
# we print the name of the first student at the course
print(course1.show_average())  # average from Luca and Mihaela
course1.add_student(s3)  # here we try to add over the course limit
