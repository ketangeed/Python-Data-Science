# 15.Write a program to read a year and check whether it is a leap year or not.

# When writing an if-elif-else structure, always put the most strict, specific condition at the very top.

year = int(input("Enter the year : "))

if (year % 400 == 0):
    print("It is a Leap Year..")

elif (year % 100 == 0):
    print("Not a Leap Year..")

elif (year % 4 == 0):
    print("It is a Leap Year..")

else:
    print("It is not a leap Year..")