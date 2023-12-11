""" Operators:

Arithmetic: +, -, *, / (gives float), // (gives int), % (modulo, return remainder), ** (to the power of)
Comparison/Relational: >, <, >=, <= (less or equal), ==(egal) != (different)
    they return True or False
Logical: and (if both True),  or  (if one True), not (reverse True/False)
Assignment: =, += (augmented assign, increases value by...)
Identity/Membership: is;  is not (if something is in something)
"""
# a=3
# b=5
# a=b
# print (a%b)
# print(12>a)
# print( a>=b)
# print (a!=b) # 5 different from 5, return False
# print (10-a==b)
# print(10//3)
# print(10/3)
print(10**3)
print(pow(10, 3))  # 10 to the power of 3 with function pow
# x=10
# x+=3 # augmentes assign, x becomes x+3
# print(x)
# print("-----------------")
# print (7>b and (b<10 or 5>10) ) # brackets for separating logical comparison
# print ((7>b or 7<b))
# print(not b>2)
# print(not b>2 and b>3)
# print("--------------")

# in school you either have to come with mom or dad or with both your grandparents
mom = False
dad = False
grandpa = True
grandma = True

print(mom or dad or (grandpa and grandma))

# Operator precedence: not > and > or !
