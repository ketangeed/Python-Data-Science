# 45. Write a program to display all prime numbers from 1 to n.

n = int(input("Enter the number: "))
count = 0
for num in range(1, n + 1):
    if num <= 1:
        continue
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime == True:
        print(num)
        count += 1
print("counts = ",count)

    