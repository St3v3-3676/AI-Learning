from models.study_question import StudyQuestion
from models.quiz_result import QuizResult

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

    def mark_quiz(self, student_answers: list[str]) -> QuizResult:
        if len(student_answers) > len(self.questions):
            raise ValueError(f"There are too many answers submitted. There should only be a maximum of {len(self.questions)} answers")
        total_score: int = 0
        for question, answer in zip(self.questions, student_answers):
            marks_awarded: int = question.evaluate_answer(answer)
            total_score += marks_awarded

        quiz_result: QuizResult = QuizResult(self.calculate_quiz_total_marks(),total_score)
        return quiz_result
