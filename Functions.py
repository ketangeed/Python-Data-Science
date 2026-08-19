# Tast : Write a Function take one parameter and and return it and print it...

def cal_sqr(number):
    return number ** 2
ans = cal_sqr(4)
print(f"The square is {ans}.")


# Task : Take one parameter and check whether it is Even or not, if yes then return True if not then false.

def is_even(num):
    if num % 2 == 0:
        return True
    else :
        return False

check = is_even(7)
print(check)


# Task : with and without the argument solve the default parameter function que..

def greeting (name, greeting = "hello"):
    return f"{greeting} {name}"

msg1 = greeting("Alex")
msg2 = greeting("Alex", "Welcome")
print(msg1)
print(msg2)




# 
def process_user_data(raw_name, birthyear):
    a = raw_name.strip().capitalize()
    ag = int(birthyear)
    age = 2026 - ag
    if age >= 18:
        status = "Adult."
    else :
        status = "Minor."

    return f"User {a} is {age} years old {status} : ."

result = process_user_data("   aLEXANder  ", "2000")
print(result)
    


scores = [("Alice", 85), ("Bob", 92), ("Charlie", 78)]

# Sort by the second element (score at index 1)
sorted_scores = sorted(scores, key=lambda item: item[1])

print(sorted_scores)