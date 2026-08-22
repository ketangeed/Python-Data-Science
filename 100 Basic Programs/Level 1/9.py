# 9.Write a program to read the marks of 5 subjects and print the total and average

sub1 = int(input("Enter the marks of English : "))
sub2 = int(input("Enter the marks of Maths : "))
sub3 = int(input("Enter the marks of Physics : "))
sub4 = int(input("Enter the marks of Chemistry : "))
sub5 = int(input("Enter the marks of Social Studies : "))


total = sub1 + sub2 + sub3 + sub4 + sub5
avg = total / 5

print(f"{total} / 500")
print(f"{avg} % ")