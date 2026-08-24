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


# string = input("Enter the String : ")
# Uppercase =  0
# Lowercase = 0
# Digits = 0
# Special = 0

# for i in string:
#     if i.isupper():
#         Uppercase += 1
#     elif i.islower():
#         Lowercase += 1
#     elif i.isdigit():
#         Digits += 1
#     else :
#         Special += 1
# print(Uppercase)
# print(Lowercase)
# print(Digits)
# print(Special)




# Given a string, find the first character that appears only once.
# Example 1
# Input:
# swiss
# Output:
# w

# string_2 = input("Enter the String : ")

# freq = {}

# # Step 1: Count frequency of each character
# for i in string_2:
#     if i in freq:
#         freq[i] += 1
#     else:
#         freq[i] = 1

# # Step 2: Find the first unique character
# found = False

# for i in string_2:
#     if freq[i] == 1:
#         print(i)
#         found = True
#         break

# # Step 3: If no unique character was found
# if not found:
#     print("No Unique Character")


# string_3 = input("Enter the String : ")
# commit = ""
# for i in string_3:
#     if i not in commit:
#         commit += i

#     else :
#         continue
# print(commit)



# Write a program that takes a string and finds the character that occurs the maximum number of times.
# Input:
# programming
# Output:
# r → 2


# n = "banana"
# freq = {}
# for i in n:
#     if i in freq:
#         freq[i] += 1
#     else:
#         freq[i] = 1
# print(max(freq))




# Q1 — Count vowels
# Take a string from the user and count the number of vowels

s = input("Enter the String : ")
vowels_ = "aeiou"
vowels = 0
consonants = 0

for i in s :
    if i in vowels_:
        vowels += 1
    elif i.isalpha():
        consonants += 1
    else:
        pass
print(vowels)
print(consonants)