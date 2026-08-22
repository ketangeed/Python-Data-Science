# 48. Write a program to display all Armstrong numbers from 1 to n.

# n = int(input("Enter the number : "))


# for i in range(1, n + 1):
#     original = i
#     var = 0
#     temp = i

#     while temp > 0:
#         digits = temp % 10
#         remainder = digits ** 3
#         var += remainder
#         temp = temp // 10

#     if var == original:
#         print(original)






# Write a program to print all the numbers from 1 to 20 that can be divided perfectly by 3.


n = input("Enter the number : ")
count = 0
for i in n:
    i = int(i)
    count += i
print(count)
