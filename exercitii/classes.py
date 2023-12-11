import datetime
class User:
    """ Here you write a doc string to acces later
    using the help(Class) function
    so you have acces to info quick
    you also get info about constructor"""
    def __init__(self, full_name, birthday):
        self.name = full_name
        self.birthday = birthday  # yyyymmdd

        #extract first and last names
        name_pieces = full_name.split (" ")
        self.first_name = name_pieces[0]
        self.last_name = name_pieces [-1]

    def age(self):
        """Returns the age of the user in years"""
        today = datetime.date(2023, 12, 8)
        yyyy = int(self.birthday[0:4])
        mm = int(self.birthday[4:6])
        dd = int(self.birthday[6:8])
        dob = datetime.date(yyyy, mm, dd)
        age_in_days = (today-dob).days
        age_in_years = age_in_days / 365
        return int(age_in_years)

#user1 is an object of the class User:
user1 = User("Dave Carlos", "19970718")

# we can add Atributes/ Fields to the specific instance later

print(user1.first_name, user1.last_name)
print(user1.age())
# help(User)

today = datetime.date.today()
yesterday = datetime.date(2023, 12, 7)
print(today)
diff = today - yesterday
print(diff.days)

