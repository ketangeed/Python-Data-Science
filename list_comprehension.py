# with condion [expression for item in data if condition]
# without codition [expression for item in data]


# numbers = [1, 2, 3, 4, 5, 6]
# sqr =[]
# for i in numbers:
#     sqr.append(i **2 )
# print(sqr)

# this is the normal method..

# and this is the list comprehension..
# a = [x ** 2 for x in numbers]
# print(a)


# create the even number comprehesioned list
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# b = [x for x in numbers if x % 2 == 0]
# print(b)


# contain only sqr of the 60 or above marks

marks = [45, 78, 92, 33, 65, 88, 29, 95]

c = [x ** 2 for x in marks if x >= 60]
print(c)

# here x ** 2 is expression ...
# x >= 60 is the condition ...