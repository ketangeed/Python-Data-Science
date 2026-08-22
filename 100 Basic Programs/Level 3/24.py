# 24.Write a program to display all odd numbers from 1 to n.

n = int(input("Enter the number : "))

for i in range(1, n+1):
    if i % 2 != 0:
        print(i)
    else:
        pass

for i in range(1, n+1, 2):
    print(i, end=" ")