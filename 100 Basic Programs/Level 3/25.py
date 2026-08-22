# 25. Write a program to find the sum of all natural numbers from 1 to n.

n = int(input("Enter the Number : "))
add = 0

for i in range (1, n+1):
    add += i

print(add)