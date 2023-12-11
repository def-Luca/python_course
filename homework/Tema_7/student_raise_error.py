# make a custom error based on another error
class GradeTooHigh(ValueError):
    pass


class Student:
    def __init__(self, name, grade):
        self.name = name
        if grade > 10 or grade < 0:
            # here you raise the custom error
            # in brackets extra info or parameter which raised error
            raise GradeTooHigh(grade)
        else:
            self.__grade = grade

    @property
    def grade(self):
        return self.__grade

    @grade.setter
    def grade(self, new_grade):
        if new_grade > 10 or new_grade < 0:
            # here you raise the custom error
            # in brackets extra info or parameter which raised error
            raise GradeTooHigh(new_grade)
        else:
            self.__grade = new_grade


stud = Student("Luca", 11)
stud.grade = 7
print(stud.grade)
