# 4.Write a program to read the radius of a circle and print its area and circumference.


r = int(input("Enter the radius of the circle : "))

print(2 * 3.14 * r)
# circumference is the distance around the cicle..
# formulae 2pyr

d = r*r
print (3.14 * d )
#   or
print(3.14 * r * r)
# area of the circle is the space inside the circle...
# formulae is py r*r(sqr)



# here is more clean version 

import math

r1 = int(input("Enter the radius of the circle : "))

circumference = 2 * math.pi * r1
area = math.pi * (r1 ** 2)

print(circumference)
print(area)