# 3.Write a program to read two numbers and print their sum, difference, product and quotient

try :
    a = int(input("enter the 1st number : "))
    b = int(input("enter the second number : "))

    print(f"the sum is = {a + b}.")
    print(f"the difference is = {a - b}.")
    print(f"the product is = {a * b}.")
    print(f"the quetient is = {a // b}.")

except ValueError:
    print("Wrong Value is Given....")

except ZeroDivisionError:
    print("Cannot divide by zero.")
