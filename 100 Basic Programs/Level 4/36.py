# 36. Write a program to find the product of all digits of a number n.

n = input("Enter the Number : ")
total_product = 1

for i in n:
    num = int(i)
    total_product *= num

print(total_product)

