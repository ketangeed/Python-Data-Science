import json

# student = {
#     "name": "Ketan",
#     "marks": 90,
#     "branch": "AIML"
# }

# Use json.dumps() to convert student into JSON and store it in a variable called data.
# Then print.
# data
# type(data)
# Don't use dump() yet. We're doing dumps() first.

# data = json.dumps(student)
# print(data)
# print(type(data))


# so json.dumps when to convert python string to json str
# and json.loads when we want convert json str to python object..


# data = '{"name": "Ketan", "marks": 85, "branch": "AIML"}'

# student = json.loads(data)
# print(student)
# print(type(student))


# now for files...
student = {
    "name": "Ketan",
    "marks": 90,
    "branch": "AIML"
}


# we we work with files use dump to json str and load to python object..
with open("json.data", "w") as file :
    json.dump(student, file)


# now to load a json str in python obj...


with open("student.json", "r") as file2:
    data = json.load(file2)
print(data)
print(type(data))
