# Task:

# Create a list named colors containing three strings: "red", "green", and "blue".

# Add "yellow" to the end of the list using .append().

# Print the first item of the list using index 0.

# colors = ["red", "green", "blue"]
# colors.append("yellow")
# print(colors)


# # change the item...

# fruits = ["apple", "banana", "cherry"]

# fruits[1] = "mango"
# fruits.insert(0, "orange")
# print(fruits)


# numbers = [10, 20, 30, 40, 50, 60, 70, 80]

# numbers.remove(30)
# print(numbers)
# numbers.pop(3)
# print(numbers)
# print(len(numbers))
# print(numbers[::-1])



# Q1 — Basic Data Processing
# Given:
# marks = [45, 78, 92, 56, 33, 89, 67, 74]
# Write a program that:
# Finds how many students passed.
# Passing marks = 40
# Prints the total number of passed students.


# marks = [45, 78, 92, 56, 33, 89, 67, 74]
# passed = []
# for i in marks:
    
#     if i >= 40:
#         passed.append(i)
#     else:
#         continue
# print(len(passed))



# find the highest value..

# temperatures = [32, 35, 31, 38, 36, 34, 39, 33]
# high = 0

# for i in temperatures:
#     if i > high:
#         high = i
#     else:
#         continue
# print(high)

# # or
# print(max(temperatures))


# calculate the average : 

# marks = [80, 65, 90, 75, 85]
# a = 0
# for i in marks:
#     a += i
# b = a / len(marks)
# print(b)


# count the marks >= 80 and marks < 40

# marks = [45, 78, 92, 56, 33, 89, 67, 74, 28, 95]
# count_above_80 = 0
# count_below_40 = 0
# for i in marks:
#     if i >= 80:
#         count_above_80 += 1
#     elif i < 40:
#         count_below_40 += 1
#     else:
#         continue
# print(count_above_80)
# print(count_below_40)


# find the minimun..
# temperatures = [32, 35, 31, 38, 36, 34, 39, 33]
# minimum = temperatures[0]
# for i in temperatures:
#     if i < minimum:
#         minimum = i 
        
# print(minimum)



# now  find both max and min..


# temperatures = [32, 35, 31, 38, 36, 34, 39, 33]
# maximum = temperatures[0]
# minimum = temperatures[0]
# for i in temperatures:
#     if i > maximum:
#         maximum = i
#     if minimum > i:
#         minimum = i
# print(f"Maximum : {maximum}")
# print(f"Minimun : {minimum}")



# find how many students have scored more than an average...

# marks = [80, 65, 90, 75, 85, 40, 95, 60]
# summ = 0
# count = 0
# for i in marks:
#     summ += i
# total = summ
# avg = total / len(marks)

# for i in marks : 
#     if i > avg :
#         count += 1

# print(count)
# print(summ)
# print(avg)



# data cleaning :

marks = [85, -10, 72, 105, 90, 67, -5, 88]
clean_marks = []

for i in marks:
    if i >= 0 and i <= 100 :
        clean_marks.append(i)
print(clean_marks)