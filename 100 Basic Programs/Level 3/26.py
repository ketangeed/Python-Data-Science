# 26. Write a program to find the sum of all even numbers from 1 to n.

n = int(input("Enter the Number : "))
add = 0
for i in range (1, n+1):
    if i % 2 == 0:
        add += i
print(add)
