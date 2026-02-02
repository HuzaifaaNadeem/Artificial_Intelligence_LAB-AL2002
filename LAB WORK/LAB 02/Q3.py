class Student:
    def __init__(self, name):
        self.name = name
        self.__marks = 0
    def set_marks(self, marks):
        self.__marks = marks
    def get_marks(self):
        return self.__marks
    def calculate_grade(self):
        if self.__marks >= 85:
            return "A"
        elif self.__marks >= 70:
            return "B"
        elif self.__marks >= 50:
            return "C"
        else:
            return "F"

student1 = Student("Ali")
student2 = Student("Sara")
student1.set_marks(88)
student2.set_marks(72)
print("Student Name:", student1.name)
print("Marks:", student1.get_marks())
print("Grade:", student1.calculate_grade())
print()
print("Student Name:", student2.name)
print("Marks:", student2.get_marks())
print("Grade:", student2.calculate_grade())
