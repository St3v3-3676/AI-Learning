from reports import Report

class TeacherReport(Report):
    def __init__(self):
        self.report = "Teacher performance report."

    def generate_report(self):
        return self.report

