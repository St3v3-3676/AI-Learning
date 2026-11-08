from study_question import StudyQuestion

class Quiz:
    def __init__(self, title: str, questions: list[StudyQuestion]) -> None:
        if len(questions) < 1:
            raise ValueError("There must be at least one question in the quiz")

        self.title = title
        self.questions = questions

    def calculate_quiz_total_marks(self) -> int:
        total_marks: int = 0
        for each_question in self.questions:
            total_marks += each_question.max_mark

        return total_marks