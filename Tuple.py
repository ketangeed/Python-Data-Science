# t = (3, 4, 6, 7, 1, 3)

# print(t.count(3)) # used to find the occurences.
# print(t.index(3)) # used to find idx of 1st occurence. 

# # they are faster than list. cause they are immutable.


# coordinates = (10, 20, 30)
# print(coordinates[1])
# print(len(coordinates))


# person = ("Alex", 25, "Developer")

# name, age, job = person

# print(f"{name} is a {age}-year-old {job}.")




# Given:
# data = (10, 20, 30, 20, 40, 20, 50)
# Find:
# How many times 20 occurs.
# The position of the first 20.

# data = (10, 20, 30, 20, 40, 20, 50)

# print(data.count(20))
# print(data.index(20))


# convert tuple into list modify it and again convert it to tuple..

data = (10, 20, 30, 40, 50)

d = list(data)

d[2] = 35

data_ = tuple(d)
print(data_)



# store the tuple values..
data = ("Ketan", 20, "AIML")
name, age, branch = data
print(f"Name : {name}\nAge : {age}\nBranch : {branch}")