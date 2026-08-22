# 17.Write a program to read a character and check whether it is an alphabet, digit or special symbol.

string = input("Enter the string : ")

for i in string :
    if i.isalpha():
        print(f"{i} is an Alphabet")
        
    elif i.isdigit():
        print(f"{i} is a Digit")

    else :
        print(f"{i} is Special symbol..")