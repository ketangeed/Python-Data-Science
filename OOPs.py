class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def intro (self):
        return f"{self.name} = {self.marks}"
s1 = Student("Ketan", 85)
print(s1.intro())

s2 = Student("Rahul", 72)
print(s2.intro())

s3 = Student("Amit", 91)
print(s3.intro())