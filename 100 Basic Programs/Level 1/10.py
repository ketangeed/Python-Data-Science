# 10.Write a program to read seconds and convert them into hours, minutes and seconds


# total_seconds = int(input("Enter the seconds : "))

# hours = total_seconds // 3600

# leftover_sec = total_seconds % 3600

# minutes = leftover_sec // 60

# seconds = leftover_sec % 60

# print(f"{hours}:{minutes}:{seconds}")



# Imagine you are writing the code for an ATM. A customer comes to the ATM and wants to withdraw a specific amount of money, let's say Rs. 7800.
# 2000, 500, 100


cash = int(input("Enter the withdraw Amount : "))


two_th = cash // 2000 # how much units fit into this
left_money = cash % 2000 # leftover money


five_hun = left_money // 500 # how much units fits into this
left_money_2 = left_money % 500 # how much is left from this


one_hun = left_money_2 // 100

print(f"2000 : {two_th} \n500 : {five_hun} \n100 : {one_hun}")

