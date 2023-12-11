# strings are a sequence of characters in quotation marks
# they cannot be modified

alphabet = "abc"
alphabet = "abcdefghb"  # overriding the variable is the only way to modify it
#          01234..-1  they are indexed from left to right or right to left(-1)
print(alphabet[0], alphabet[3])  # a and d
print(alphabet[-1])  # h
print(alphabet.index("b"))  # 1 shows the first index of a substring sequence

# they have methods which can be called
# methods don't modify the string
course = "Imi place sa programez"

print(course.upper())  # face toate literele mari
print(course.lower())  # face toate literele mici
print(course)  # stringul original ramane identic

print(course.find("p"))  # 4 the first index of "p", if no occurence returns -1
print(course.rfind(""))  # 20 last index of the "e"

print(course.replace(" ", "_"))  # replaces

print("place" in course)  # in returns True if the substring is in the stirng

print(course.count("a"))  # how many a's in curs
print("----------------")

"""string operations:
Concatenation: append a string onto another with "+" sign
Enumerat: enumerate strings with comma
Formated string: f"my_string {other_variable}"""

s1 = "abc"
s2 = "123"
s3 = "def"
number = 3

print(s1 + s2)  # Concatenation
print(s2, s3)  # Enumeration
print(f"first {number} numbers in the alphabet are {s1} {True} ")

# OR format function
string = "{}-{}, {}"
print(string.format("Luca", "Marian", "Ioan"))

# join function
print("-".join("def"))  # returns a string with elements joined by an element
