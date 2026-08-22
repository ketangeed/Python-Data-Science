# 2.Write a program to read two numbers and print their sum. 

# a = int(input("Enter the first Numbers : "))
# b = int(input("Enter the second number : "))

# c = (a+b)

# print(c)

a = int(input("num 1 :"))
b = int(input("num 2 :"))
print(a + b)



#  more clean version

try:
    a = int(input("Num 1: "))
    b = int(input("Num 2: "))
    print(f"The sum is: {a + b}")
except ValueError:
    print("❌ Error: Please enter valid integer numbers!")