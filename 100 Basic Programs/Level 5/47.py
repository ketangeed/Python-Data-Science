# 47. Write a program to check whether a number is an Armstrong number.


num = int(input("Enter the number : "))
original = num 
var = 0

while num > 0:
    digit = num % 10
    remainder = digit ** 3
    var += remainder
    num = num // 10

if original == var:
    print("Armstrom")
else:
    print("Not Armstrom")