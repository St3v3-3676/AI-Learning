from reports import Report

class StudentReport(Report):
    def __init__(self):
        self.report = "Student progress report."

    def generate_report(self):
        return self.report