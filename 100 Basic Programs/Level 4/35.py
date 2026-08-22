# 35. Write a program to find the sum of all digits of a number n.

n = input("Enter the Number : ")
total_sum = 0

for i in n:
    num = int(i)
    total_sum += num

print(total_sum)