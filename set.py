# raw_numbers = [1, 2, 2, 3, 4, 4, 4, 5]

# unique_numbers = set(raw_numbers)
# print(unique_numbers)

# fruits = {"apple", "banana"}
# fruits.add("cherry")
# print(fruits)



# usernames = {"admin", "user1", "dev_guy"}
# a = usernames.discard("user1")
# print(usernames)


# data = [10, 20, 10, 30, 20, 40, 50, 30, 10]
# unique_data = set(data)
# print(unique_data)


# Find the common courses...
# Two students attended different courses:
# Find the students who are in both courses.


python_students = {"Ketan", "Rahul", "Amit", "Priya", "Rohan"}
ml_students = {"Amit", "Priya", "Sneha", "Rohan", "Vikas"}
print(python_students.intersection(ml_students))


# Find the differece : 
python_students = {"Ketan", "Rahul", "Amit", "Priya", "Rohan"}
ml_students = {"Amit", "Priya", "Sneha", "Rohan", "Vikas"}
print(python_students.difference(ml_students))