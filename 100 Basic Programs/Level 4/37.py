# 37. Write a program to reverse a number n.

n = input("Enter the Number : ")

# reverse_n = 0

# for i in range(-1):
#     reverse_n += i
# print(reverse_n)
    
print(n[::-1])



#  OR


num = int(input("Enter the Number: "))
reversed_num = 0


while num > 0 :
    remainder = num % 10
    reversed_num = (reversed_num * 10) + remainder
    num = num // 10
    if reversed_num == num:
        print("palindrome")
print(reversed_num)