class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def intro (self):
        return f"Name : {self.name}\nMarks : {self.marks}"
s1 = Student("Ketan", 85)
print(s1.intro())

