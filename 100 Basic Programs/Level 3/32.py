# 32. Write a program to display all numbers from 1 to n that are divisible by 3 or 5.

n = int(input("Enter the number : "))
count = 0

for i in range(1, n+1):
    if i % 3 == 0 or i % 5 == 0:
        count += 1

print(count)

#  OR Gemini que
num = int(input("Enter the Number : "))

digit = 0

while num > 0:
    num = num // 10
    digit += 1
print(digit)