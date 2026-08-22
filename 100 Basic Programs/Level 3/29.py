# 29. Write a program to display the multiplication table of a number n.

n = int(input("Enter the Number : "))

for i in range (1, 11):
    print(n, "x", i, "=", n*i)