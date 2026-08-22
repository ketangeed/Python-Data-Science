# 44. Write a program to read a number and check whether it is prime or not.

num = int(input("Enter the Number :  "))

if num <= 1:
    print("This is not a prime number ..")
else:
    is_prime = True

    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime == True:
        print("This is the prime number..")
    else:
        print("This is not a Prime Number ..")
