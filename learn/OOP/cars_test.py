from cars_def import Car
# if modules in the same folder you can get from folder import Class

EQS = Car("EQS", "white", True)
e_class = Car("e_class", "black")

print(EQS.mark, EQS.model, EQS.colour)

EQS.paint("red")   # we change the attribute colour
print(EQS.colour)
print(e_class.colour)     # e_class mantains the black colour

s_class = Car("s_class", "red", True)
s_class.electric_windows()  # here we create the new attribute for s_class
print(s_class.windows)
print(s_class.leather)

s_class.accelerate()
s_class.brake()
