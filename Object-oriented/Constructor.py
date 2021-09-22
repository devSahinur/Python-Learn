# constructor __init__ function

class Student:
    roll = ""
    gpa = ""

    def __init__(self,roll,gpa):
        self.roll = roll
        self.gpa = gpa

    def display(self):
        print(f"Roll: {self.roll}, GPA : {self.gpa}")

rahim = Student(101,3.74)
# rahim.set_value()
rahim.display()

sahinur = Student(102,2.98)
# sahinur.set_value(102,2.98)
sahinur.display()