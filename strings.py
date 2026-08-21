# Write a program that takes a string and counts:
# uppercase letters
# lowercase letters
# digits
# special characters

# Input:
# "PyThOn123@#"
# Output:
# Uppercase: 3
# Lowercase: 3
# Digits: 3
# Special: 2


string = input("Enter the String : ")
Uppercase =  0
Lowercase = 0
Digits = 0
Special = 0

for i in string:
    if i.isupper():
        Uppercase += 1
    elif i.islower():
        Lowercase += 1
    elif i.isdigit():
        Digits += 1
    else :
        Special += 1
print(Uppercase)
print(Lowercase)
print(Digits)
print(Special)