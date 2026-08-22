# 5.Write a program to read the length and breadth of rectangle and print its area and perimeter
a = int(input("Enter the length of Rectangle : "))
b = int(input("Enter the breath of Rectangle : "))


print(f"the area of Rectangle is {a * b}.")
# space inside the rectangle


print(f"the perimeter of the Rectangle is {2 * (a + b)}")
# perimeter is the distance around the rectangle...



#  or

length = int(input("Enter the length of Rectangle: "))
breadth = int(input("Enter the breadth of Rectangle: "))

# Clean, self-explanatory calculations
area = length * breadth
perimeter = 2 * (length + breadth)

print(f"The area of the Rectangle is {area}.")
print(f"The perimeter of the Rectangle is {perimeter}.")