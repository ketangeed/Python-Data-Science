# 7.Write a program to swap two numbers without using a third variable.

a = int(input("enter the number : "))
b = int(input("enter the number : "))


# let a = 5, b = 10


a = a + b # here now a is 15
b = a - b # here b is 15 - 10 = 5, original a has been swaped
a = a - b # and now here a is 10

print(a)
print(b)