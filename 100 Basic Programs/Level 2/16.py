# 16.Write a program to read a character and check whether it is a vowel or a consonant.



word = input("Enter the String : ")
vowels = ['a','e','i','o','u']

vowels_in_word = []
vowel_count = 0
consonant_count = 0

for i in word:
    if i.lower() in vowels:
        vowels_in_word.append(i)
        vowel_count += 1
    else:
        consonant_count += 1

print(vowels_in_word)
print(vowel_count)
print(consonant_count)


