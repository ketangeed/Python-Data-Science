# class Student:
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks
#     def intro (self):
#         return f"{self.name} = {self.marks}"
# s1 = Student("Ketan", 85)
# print(s1.intro())

# s2 = Student("Rahul", 72)
# print(s2.intro())

# s3 = Student("Amit", 91)
# print(s3.intro())



# class Students:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     def result(self):
#         if self.marks >= 40:
#             return "Pass"
#         else:
#             return "Fail"

# stu1 = Students("Ketan", 89)
# print(stu1.result())

# stu2 = Students("Rahul", 32)
# print(stu2.result())


# Inheritance :
class Animal:
    def speak(self):
        print("Animal Makes a sound..")
class dog(Animal):
    def speak(self):
        print("Woof!!!")

d = dog()
d.speak()


# super ()

class Student:
    def __init__(self, name):
        self.name = name

class boy(Student):
    def __init__(self, name, marks):
        super().__init__(name)
        self.marks = marks

b = boy("Ketan", 98)
print(b.name)
print(b.marks)