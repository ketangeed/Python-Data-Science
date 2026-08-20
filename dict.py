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


d = {"a": 10, "b": 20, "c": 30, "d": 40}
a = 0
for i in d.values():
    a += i
    b = a/4
print(b)