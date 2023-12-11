def wrong_answer():
    print("wrong answer")


def right_answer():
    print("correct, you get a point")


print("welcome to my quiz game do you want to play? ")
access = input("q for quit, everything else starts! ").lower()
s = 0
if access == "q":
    print("Have a gread day!")
    quit()
print("let's go!")
geography = input("What's the capital of Russia ? ").lower()
if geography == "moscow":
    right_answer()
    s += 1
else:
    wrong_answer()
physics = input("is it true that water boils at 100 degrees Celsius? y for yes ").lower()
if physics == "y":
    right_answer()
    s += 1
else:
    wrong_answer()
literature = input("who wrote the art of war ? ").lower()
if literature == "sun tzu":
    right_answer()
    s += 1
else:
    wrong_answer()
maths = input("how much is (3 + 4 * 5) ? ")
if maths == "23":
    right_answer()
    s += 1
else:
    wrong_answer()
if s == 0:
    print("sorry you got 0 points")
else:
    print(f"Congratulations you got {s} out of 4 questions right")
