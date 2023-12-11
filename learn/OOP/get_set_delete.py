"""we use getter setter and deleter to act on private attributes
and also when we want attributes of the object to dinamically change"""

class Employee:
    def __init__(self, first, last):
        self.__first = first
        self.__last = last

    # property decorator converts to an attribute the return of the method
    @property
    def email(self):
        return "{}.{}@gmail.com".format(self.__first, self.__last)
        # acum return din functia email este atribut!

    # we can use multiple property decorators
    @property
    def fullname(self):
        return "{} {}".format(self.__first, self.__last)

    @fullname.setter
    def fullname(self, new_name):
        first, last = new_name.split(" ")
        self.__first = first
        self.__last = last

    @fullname.getter
    def fullname(self):
        return self.__first, self.__last

    @fullname.deleter
    def fullname(self):
        print("delete name")
        self.__first = None
        self.__last = None


emp_1 = Employee("John", "Doe")

emp_1.fullname = "Luca Ioan"  # setter

print(f"name after the change is {emp_1.fullname}")  # getter
print(emp_1.email)  # the email created is changing after the name change

print(type(emp_1.fullname))
del emp_1.fullname  # deleter

print(emp_1.fullname)