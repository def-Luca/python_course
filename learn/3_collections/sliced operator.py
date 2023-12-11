# sliced operators allows to take only a part of a n item
# sliced= item[start:stop:step] it reffers to indeces
x = [1, 2, 3, 4, 5, 6, 7, 8]
y = ["a", "b", "c", "d"]
z = "Greetings!"

sliced = x [1:6:2]
print(type(sliced))  # the type remains the same
print(sliced)
sliced_stop = x[:4]  # right to the column is the stop argument
print(sliced_stop)
sliced_step = x[1::2]  # default index is 0
print(sliced_step)

print(x[::-1])  # useful for reversing a list/string
slice_string = z[::-1]
print (type(slice_string))
print(slice_string)
