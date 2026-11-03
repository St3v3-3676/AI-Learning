class ExamReport:
    def __init__(self, subject: str):
        self.subject: str = subject

    def generate_report(self) -> str:
        return f"{self.subject} examination report"
