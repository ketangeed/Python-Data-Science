# 20.Write a program to read the age of a person and check whether they are eligible to vote.


age = int(input("Enter the AGE : "))

if age >= 18 and age <= 100:
    print("Eligible to Vote.")

else:
    print("Not eligible to Vote..")


#  OR 


age = int(input("Enter the AGE : "))

# 1. Catch impossible ages first
if age < 0 or age > 100:
    print("Invalid Age! Please enter a realistic age.")
# 2. Check voting requirement
elif age >= 18:
    print("Eligible to Vote.")
# 3. Fallback for minors (0 to 17)
else:
    print("Not eligible to Vote.")