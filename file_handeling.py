# used to write in the file:

# with open("student.txt", "w") as file:
#     data = file.write("Ketan\nAIML\nPython")
#     print(data)

# data = []
# with open("student.txt", "r") as file:
#     for line in file:
#         data.append(line.strip())
# print(data)


# here we read and create a list with it...



# to write/overwrite the file...
# with open("student.txt", "w") as file1:
#     data = file1.write("Ketan\nAIML\nPython")
#     print(data)



# with open("student.txt", "r") as file2:
#     data2 = file2.read()
#     print(data2)


# to get the output line by line..

# with open("student.txt", "r") as file2:
#     print(file2.readline())
#     print(file2.readline())
#     print(file2.readline())


# now to using for loop

# with open("student.txt", "r") as file2:
#     for file in file2:
#         print(file.strip())
# here to strip the specess..



# now we got read, readline for line by line, now it is time for the readlines,
# here it will print all the lines in list....


# with open("student.txt", "r") as file2:
#     data = file2.readlines()
#     print(data)


# append = to add the data at the end of the existing data without removing it..



# with open("student.txt", "a") as file2:
#     data = file2.write("\nData Science")
#     print(data)




# to create a new file.. 

# with open("new_student.txt", "x") as file2:
#     file2.write("Python\ndata science")
    



# Q8 — Read and clean the file

# Write code that:

# Opens student.txt in "r" mode.
# Loops through every line.
# Removes \n using .strip().
# Adds each cleaned line into an empty list called data.
# Prints data.


data = []
with open("student.txt", "r") as file:
    for line in file:
        data.append(line.strip())
print(data)
        