# text files> .txt extension.
# syntax is with open("C:\user\...location in computer..\text_file_name", "mode")
# there are many modes to open the text file

    # many read functions



# opening and creating a text file in write mode
with open("my_first_file.txt", "w") as file:
    file.write("Python written text")
# if we run this multiple times we don't get the text multiplied
# because the content will be overridden each time

with open("my_first_file.txt", "a") as file:
    file.write(" appending this text")
# here we append the input to the text
# or creates new file if not already

#opening a text file in read mode
# raise FileNotFoundError if no file
with open("my_first_file.txt", "r") as file:
    file_content = file.read()

# outside "with" the file is closed, almost like a a while loop
print(file_content)  # printing the read content from text file

"""CSV - Comma separated Values files
these files have a structure where each value is separated by a comma
is like a table
TSV - Tab separated Values is similar"""
import csv
# csv not suported by pycharm comunity
with open ("my_first_csvfile.csv", "w") as table:
    csv_reader = csv.reader(table)
