# 41. Write a program to check whether a number n is a palindrome (reads the same reversed).

n = int(input("Enter the number : "))

reversed_n = 0

while n > 0:
    remainder = n % 10
    reversed_n = (reversed_n * 10) + remainder
    n = n // 10
    if reversed_n == n:
        print("The Number is Palindrome...")
  
