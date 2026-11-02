from student import Student
from teacher import Teacher

class Classroom:
    def __init__(self, teacher: Teacher):
        self.teacher = teacher
        self.students: list[Student] = []

    def add_student(self, student: Student):
        self.students.append(student)

teacher1 = Teacher("Sarah", 35, "Computer Science")
classroom1 = Classroom(teacher1)

student1 = Student("0001", "Alex", 16, 10)
student2 = Student("0001", "Emma", 15, 10)

print(student1.student_id)
student1.student_id = 2001