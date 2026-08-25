# used to write in the file:

# with open("student.txt", "w") as file:
#     data = file.write("Ketan\nAIML\nPython")
#     print(data)

data = []
with open("student.txt", "r") as file:
    for line in file:
        data.append(line.strip())
print(data)


# here we read and create a list with it...

