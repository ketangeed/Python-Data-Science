# 40. Write a program to count the number of even digits and odd digits in a number n.

n = input("Enter the Number : ")

even_digit = 0
odd_digit = 0

for i in n:
    num = int(i)
    if num % 2 == 0:
        even_digit += 1
    else:
        odd_digit += 1

print(f"Even no = {even_digit}")
print(f"Odd no = {odd_digit}")