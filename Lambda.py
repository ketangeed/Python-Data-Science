# lambda arguments: expression
# ex..
# a = lambda x : x**2
# print(a(5))
# here the x is input(argument)
# and x ** 2 is output(expression)

# this will return True/False

# b = lambda x: x > 50
# print(b(70)) # ...True
 


# q. take lambd function and return its cube..
# cube = lambda x : x ** 3
# print(cube(5))

# now takes 2 argument and return their sqr

# square = lambda x, y : x * y
# print(square(5, 7))




# Create a lambda function called is_pass that returns:
# True if marks are 40 or above
# False otherwise

# marks = [45, 72, 91, 63, 88]

# is_pass = lambda i: i >= 40 
# print(is_pass(63))

# passed = list(map(lambda x : x >= 40, marks))
# print(passed)

#  add 5 to evry number :
 

# numbers = [10, 20, 30, 40, 50]

# add = list(map(lambda x : x + 5, numbers))
# print(add)