# Write a program that takes a student's marks and prints:

# 90–100 → Excellent
# 75–89  → Very Good
# 60–74  → Good
# 40–59  → Pass
# Below 40 → Fail


# marks = int(input("Enter the Marks : "))

# if marks < 0 or marks > 100 :
#     print("Invalid Marks...")
# elif marks >= 90:
#     print("Excellent...")
# elif marks >= 75:
#     print("Very Good..")
# elif marks >= 60:
#     print("Good...")
# elif marks >= 40:
#     print("Pass..")
# else:
#     print("Fail...")



# Now Use Fucntion and return the Student marks Status...
# def grade(marks):
#     if marks < 0 or marks > 100 :
#         return "Invalid Marks..."
#     elif marks >= 90:
#         return "Excellent..."
#     elif marks >= 75:
#         return "Very Good.."
#     elif marks >= 60:
#         return "Good..."
#     elif marks >= 40:
#         return "Pass.."
#     else:
#         return "Fail..."

# result = grade(95)
# print(result)


# Create a function:
# count_vowels(text)

# It should:
# Take a string
# Count the vowels (a, e, i, o, u)
# Handle uppercase letters too
# Return the number of vowels

# def count_vowels(name):
#     vowels = "aeiou"
#     count = 0

#     for i in name.lower():
#         if i in vowels:
#             count += 1
#     return count
    
# print(count_vowels("Hello World"))



# Imagine you receive names from a dataset:
# "  rahul "
# "RAHUL"
# " Rahul"
# "rahul  "
# Your job is to create a function:
# clean_name(name)
# that:
# Removes unnecessary spaces from the beginning/end.
# Converts the name to lowercase.
# Returns the cleaned name.

# def clean_name(name):
#     return name.lower().strip()
# b = clean_name(" KETAN ")
# print(b)



# names = ["  Rahul ", "KETAN", " rahul", "Amit ", "Ketan"]

# for i in names:
#    print(clean_name(i))





# Create:
# def check_email(email):
# It should return:
# Valid
# if the email contains:
# @
# .
# and @ comes before .
# Otherwise return:
# Invalid


# def check_email(email):
#     at_position = email.find("@")
#     dot_position = email.find(".")
#     if at_position < dot_position and at_position != -1 and dot_position != -1:
#         return "Valid.."

#     else:
#         return "Invalid..."


# mail = check_email("keta@gmail.com")
# print(mail)






# names = ["  Rahul", "KETAN ", " amit ", "ROHAN", "  Priya  "]



# def cleaned_names(list):
#     cleaned = []
#     for i in list:
        
#         a = i.lower().strip()
#         cleaned.append(a)
#     return cleaned

# data = cleaned_names(names)
# print(data)




# filter even

# numbers = [12, 5, 8, 21, 30, 7, 16, 3]

# def filter_even(list1):
#     even_num = []
#     for num in list1:
#         if num % 2 == 0:
#             even_num.append(num)
#         else:
#             continue
#     return even_num

# n = filter_even(numbers)
# print(n)





# Create a list, clean it in function and remove the duplicate and return it...
# data = ["Python", "java", "PYTHON", "C++", "python", "Java"]

# def normalize_lang(d):
#     cleaned_data = []
#     # seen = set()
#     for i in d:
#         cleaned = i.lower()
#         if cleaned not in cleaned_data:
#             # seen.add(cleaned)
#             cleaned_data.append(cleaned)
#         else:
#             continue
#     return cleaned_data
    
# da = normalize_lang(data)
# print(da)




# Match Case : 

# n = input("Enter the Mean/Median/Mode : ")

# match n.lower():
#     case "mean":
#         print("You Selected Mean...")
#     case "median":
#         print("You Selected Median...")
#     case "mode":
#         print("You Selected Mode...")
#     case _:
#         print("Invalid...")



# def operation(choice):
#     match choice.lower():
#         case "mean":
#             return "You Selected Mean..."
#         case "median":
#             return "You Selected Median..."
#         case "mode":
#             return "You Selected Mode..."
#         case _:
#             return "Invalid..."
# op = operation("meaN")
# print(op)



# f-string

# name = "Ketan"
# score = 87
# subject = "Python"

# print(f"{name} scored {score} in {subject}.")

# names = "Ketan"
# scores = 87.45678
# print(f"{name} score {scores:.2f} marks.")



# Loop idx numbering...

# text = "Python"
# position = 0
# for i in text:
#     print(f"{i} = {position}")
#     position += 1

# while loop :
password = "python123"
n = ""
while n != password:

    n = input("Enter the Password : ")
    if n == password:
        print("Correct Password...")

    else:
        print("Try Again...")

