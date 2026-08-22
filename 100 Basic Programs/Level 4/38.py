# 38. Write a program to find the largest digit in a number n.

n = input("Enter the Number : ")
# print(max(n))


largest =  0


for i in n:
    num = int(i)
    if num > largest:
        largest = num
print(largest)
    