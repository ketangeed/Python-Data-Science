# 19.Write a program to read a number and check whether it is divisible by both 3 and 5.

num = int(input("Enter the number : "))

if (num % 3 == 0) and (num % 5 == 0):
    print("Num is Divisible by both 3 an 5.")
else :
    print("the num is not divisible by 3 and 5..")


#  OR

if (num % 15 == 0):
    print("Divisible by 3 and 5.")
# math shortcut