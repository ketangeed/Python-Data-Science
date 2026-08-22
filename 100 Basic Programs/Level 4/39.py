# 39. Write a program to find the smallest digit in a number n.

num = input("Enter the Number : ")
print(min(num))

smallest = 9

for i in num:
    n = int(i)
    if n < smallest:
        smallest = n
print(smallest)

