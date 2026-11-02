from person import Person
from student import Student
from teacher import Teacher
from reports import Report
from teacherReport import TeacherReport
from studentReport import StudentReport

reports: list[Report] = [TeacherReport(), StudentReport()]

for report in reports:
    print(report.generate_report())

