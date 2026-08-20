d1 = {"a": 1, "b": 2}
d2 = {"c": 3, "d": 4}

d1.update(d2)

print(d1)




word = "programming"
count = {}

for char in word:
    count[char] = count.get(char, 0) + 1

print(count)





word = "programming"

count = {}

for char in word:
    if char in count:
        count[char] += 1
    else:
        count[char] = 1

print(count)




students = {
    "Rahul": 85,
    "Priya": 92,
    "Amit": 76,
    "Sneha": 89
}


for i in students.values():
    if i > 90:
        if i == students.keys():
            print(students)