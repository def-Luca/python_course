# integer is whole number, float is with decimal place

pi = 3.14124
x = -2  # negative value assignment
age = 20
int_miliard = 1_000_000_000  # undescore for bigger numbers
float_weight = 72.9  # float > decimal number

age = float(age)  # float from integer
float_weight = int(float_weight)  # int from float you lose decimal, no rounding
print(float_weight)

print(-abs(age))  # -abs negative absolute valuea
print(abs(x))  # abs positive absolute value
print((2 + 4) / 2 * 5**2)  # al math operations are available

print(pi.__round__(3))  # rounds x.5 to x+1
# argument tells how many decimal places
print(round(pi, 2))  # same thing with round function

print(x.__add__(5))  # just an addition
