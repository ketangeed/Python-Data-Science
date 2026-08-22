# 14.Write a program to read three numbers and find the smallest among them.

num_1 = int(input("Enter the Num 1 : "))
num_2 = int(input("Enter the Num 2 : "))
num_3 = int(input("Enter the Num 3 : "))

num = min(num_1, num_2, num_3)
print(f"{num} is the smallest among the others.")

#  OR

if (num_1 <= num_2) and (num_1 <= num_3):
    print(f"{num_1} is the smallest among others.")
elif (num_2 <= num_1) and (num_2 <= num_3):
    print(f"{num_2} is the smallest among others.")
else:
    print(f"{num_3} is the smallest among others.")