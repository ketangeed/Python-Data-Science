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





# records = [("Alice", 88), ("Bob", 95), ("Charlie", 72), ("Diana", 90)]

# names = [i[0] for i in records]
# print(names)


# for i in records:
#     if i[1] >= 90:
#         print(i)
# records.append("k", 90)



# movies = [
#     ("Inception",2010, 8.8),
#     ("The Matrix",1999, 8.7),
#     ("Interstellar",2014, 8.6)
# ]

# movie_name = [i[1] for i in movies]
# print(movie_name[1])
# movies.append(("Avatar", 2009, 7.9))
# print(movies)


# for name in movies:
#     if name[1] > 2000 :
#         print(name[0])




inventory = [
    ("Laptop", 1000, 5),
    ("Mouse", 25, 50),
    ("Keyboard", 45, 0)
]

restock = [i[1] for i in inventory]
restock[2] = 60
print(restock)

for i in inventory:
    if i[2] == 0:
        print(i[0])

price = [i[1]*i[2] for i in inventory]
print(price)
print(sum(price))