# 46. Write a program to display the first n prime numbers.


n = int(input("Enter the number: "))
count = 0
num = 2

while count < n:
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime == True:
        print(num)
        count += 1

    num += 1

print("counts = ",count)

