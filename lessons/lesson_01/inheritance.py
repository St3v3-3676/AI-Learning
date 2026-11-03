from report_protocol import Reportable
from exam_report import ExamReport


def print_report(report: Reportable) -> None:
    print(report.generate_report())


exam = ExamReport("Computer Science")
print_report(exam)

