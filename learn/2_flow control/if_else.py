# if checks the if a condition is true then executes indented code
# elif, if the if condition is false python checks elif
# if none of the if or elif executed then else line gets executed
# elif and else are optional!
# you can nest if condition in one another, there is no limit

x = input("insert a 2-digit number ")
if len(x) == 2:  # checks if their input has only 2 digits
    x = int(x)
    print("2 digit number")  # prints the reslt
    if x % 2 == 0:
        # nested if condition, if 2 digit number, checks to see if it is even
        print("even number")
    else:
        print("uneven number")
else:
    print("the number is bigger than 2 digits")
