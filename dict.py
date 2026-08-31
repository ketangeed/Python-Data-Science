# d1 = {"a": 1, "b": 2}
# d2 = {"c": 3, "d": 4}

# d1.update(d2)
# print(d1)

# word = "programming"

# count = {}

# for char in word:
#     if char in count:
#         count[char] += 1
#     else:
#         count[char] = 1

# print(count)


# students = {
#     "Rahul": 85,
#     "Priya": 92,
#     "Amit": 76,
#     "Sneha": 89
# }


# for name, score in students.items():
#     if score > 90:
#         print(name)



# sentence = "python is easy and python is powerful"
# counts = {}

# for charecter in sentence:
#     if charecter in counts:
#         counts[charecter] += 1
#     else:
#         counts[charecter] = 1

# print(counts)


# data = {"a" : 78, "b": 90, "c" : 40, "d": 25}
# new_data = {}
# for ch, score in data.items():
#     if score >= 50:
#         new_data[ch] = score
# print(new_data)


# sqr = {}
# for i in range(1, 11):
#     square = i ** 2
#     sqr[i] = square
# print(sqr)




# access the keys without loop:

# student = {
#     "name": "Ketan",
#     "age": 20,
#     "branch": "AIML",
#     "marks": 87
# }

# print(student["name"])
# print(student["age"])


# change the marks form 75 to 90..
# and add key grade to A
# student = {
#     "name": "Ketan",
#     "age": 20,
#     "marks": 75
# }

# student["marks"] = 90
# student["grade"] = "A"
# print(student)


# print the name of the students who scored 80 or above:
# students = {
#     "Ketan": 85,
#     "Rahul": 72,
#     "Amit": 91,
#     "Priya": 65,
#     "Rohan": 88
# }

# for name, mark in students.items():
#     if mark >= 80:
#         print(name)
#     else:
#         continue


# count how many times the fruit appears...
# data = ["apple", "banana", "apple", "orange", "banana", "apple"]
# count = {}

# for fruit in data:
#     if fruit in count:
#         count[fruit] += 1
#     else:
#         count[fruit] = 1
# print(count)



# max_count = 0
# most_freq = ""

# for fruit, frequency in count.items():
#     if frequency > max_count:
#         max_count = frequency
#         most_freq = fruit
# print(most_freq)




# Print the name of the student with marks above 80..
# students = {
#     "Ketan": {
#         "age": 20,
#         "marks": 85
#     },
#     "Rahul": {
#         "age": 21,
#         "marks": 72
#     },
#     "Amit": {
#         "age": 20,
#         "marks": 91
#     }
# }

# for name, bio in students.items():
#     if bio["marks"] >= 80:
#         print(name)
#     else:
#         continue


# student = {
#     "name": "Ketan",
#     "marks": 85,
#     "branch": "AIML",
#     "age": 20
# }

# student = {
#     "name": "Ketan",
#     "marks": 85,
#     "branch": "AIML",
#     "age": 20
# }





# student = {
#     "name": "Ketan",
#     "marks": 85
# }


# student.update({"age" : 20})
# student.update({"marks" : 90})
# print(student)


# to remove the value
# s = student.pop("age")
# print(student)
# print(s)

# removed = student.popitem()
# print(removed)
# print(student)



# student = {
#     "name": "Ketan",
#     "marks": 90
# }

# Create a copy called student2.
# Change student2["marks"] to 100.
# Print both dictionaries.

# student2 = student.copy()
# student2["marks"] = 100
# print(student)
# print(student2)


student = {
    "name": "Ketan",
    "marks": 90
}

age = student.setdefault("age", 21)
print(age)
print(student)