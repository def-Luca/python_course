"""while loos execute the code indented
as long as the condition is true"""

x = 1
while x < 10:
    print("increase by 1 = ", x)
    x += 1
    if x % 2 == 0:
        print("even number")

run = True

while run:  #  you can declare here also True
    print("I ran a lap")
    run = bool(int(input("another lap 0 - no, 1 - yes? ")))
else:  # else executes when while loops breaks
    print("I am tired")

